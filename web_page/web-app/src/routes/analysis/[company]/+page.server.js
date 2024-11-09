import { redirect, fail } from '@sveltejs/kit';

export function load({ params, locals }) {
	let company = params.company;
    let selectedValue = locals.selectedValue || 'Select a product...';

    return { company, selectedValue };
}

export const actions = {
    selectProduct: async ({ request, locals }) => {
      const formData = await request.formData();
      const selectedValue = formData.get('selectedValue');
  
      // Validate selection
      if (typeof selectedValue !== 'string' || !selectedValue) {
        return fail(400, { error: 'Invalid selection.' });
      }
  
      // Store the selected value in `locals`
      locals.selectedValue = selectedValue;
  
      // Redirect to avoid form resubmission issues
      throw redirect(303, '/');
    }
  };