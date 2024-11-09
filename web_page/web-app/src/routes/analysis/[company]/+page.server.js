// src/routes/[company]/+page.server.js
import { redirect, fail } from '@sveltejs/kit';

let cachedData = null; // Cached data variable to store API data
let isLoading = false; // Loading flag to indicate data loading status

/** @type {import('./$types').PageServerLoad} */
export async function load({ params, locals }) {
    const company = params.company;
    const selectedValue = locals.selectedValue || 'Select a product...';

    if (cachedData) {
        // Return cached data if already fetched
        return {
            company,
            selectedValue,
            ...cachedData,
            isLoading: false
        };
    }

    // Set loading flag and start fetching data
    if (!isLoading) {
        isLoading = true;

        const apiBaseUrl = 'http://localhost:8020'; // Replace with actual API base URL

        async function fetchData(endpoint) {
            const url = `${apiBaseUrl}/${endpoint}/${company}`;
            const response = await fetch(url);

            if (!response.ok) {
                console.error(`Failed to fetch ${endpoint} data`);
                throw new Error(`Failed to load data from ${endpoint}`);
            }

            return await response.json();
        }

        try {
            // Fetch all data from API endpoints concurrently
            const [
                bestToSellData,
                popularProductsData,
                popularCategoriesData,
                pairsData,
                predictionsData
            ] = await Promise.all([
                fetchData('best_to_sell'),
                fetchData('popular_products'),
                fetchData('popular_categories'),
                fetchData('get_pairs'),
                fetchData('get_predictions')
            ]);

            // Store fetched data in cache
            cachedData = {
                bestToSellData,
                popularProductsData,
                popularCategoriesData,
                pairsData,
                predictionsData
            };

            return {
                company,
                selectedValue,
                ...cachedData,
                isLoading: false
            };
        } catch (error) {
            console.error("Error loading data:", error);
            return { error: "Failed to load data from API", isLoading: false };
        } finally {
            isLoading = false; // Reset loading flag
        }
    }

    // Return loading status if data is still being fetched
    return {
        isLoading: true
    };
}

export const actions = {
    selectProduct: async ({ request, locals, params }) => {
        const formData = await request.formData();
        const selectedValue = formData.get('selectedValue');

        if (typeof selectedValue !== 'string' || !selectedValue) {
            return fail(400, { error: 'Invalid selection.' });
        }

        locals.selectedValue = selectedValue;

        throw redirect(303, `/analysis/${params.company}`);
    }
};
