// src/routes/[company]/+page.server.js
import { redirect, fail } from '@sveltejs/kit';

/** @type {import('./$types').PageServerLoad} */
export async function load({ params, locals }) {
    const company = params.company;
    const selectedValue = locals.selectedValue || 'Select a product...';

    const apiBaseUrl = 'http://localhost:8020';

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
        // Set isLoading to true to indicate the start of data loading
        const isLoading = true;

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

        return {
            company,
            selectedValue,
            bestToSellData,
            popularProductsData,
            popularCategoriesData,
            pairsData,
            predictionsData,
            isLoading: false // Set to false once data is loaded
        };
    } catch (error) {
        console.error("Error loading data:", error);
        return { error: "Failed to load data from API", isLoading: false };
    }
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
