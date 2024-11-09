// src/routes/search/+page.server.js
export const actions = {
    default: async ({ request }) => {
      const formData = await request.formData();
      const query = formData.get("query");
  
      if (query) {
        console.log("Search Query:", query);
      }
  

    //TODO: validate query, give error if query is empty or does not exist
      return {
        query 
      };
    }
  };
  