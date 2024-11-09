from flask import Flask, request, jsonify

import best_to_sell
from best_to_sell import *
from find_pairs import *
from Items_sales_list import *
from predict_sales import *

app = Flask(__name__)


# Sample algorithm function
def sample_algorithm(data):
    # Replace this with your actual algorithm
    result = sum(data)  # Example operation
    return result


@app.route('/best_to_sell/<organization>', methods=['GET'])
def best_to_sell_algo(organization):
    try:
        result = get_low_cost_best_sell(organization)

        # Check if result is empty and handle accordingly
        if result.empty:
            return jsonify({"error": "No data available for this organization"}), 404

        # Convert to "records" orientation for easier JSON readability
        return jsonify(result.to_dict(orient="records"))
    except Exception as e:
        print(f"Error in best_to_sell_algo: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/popular_products/<organization>', methods=['GET'])
def get_list_of_popular_products_algo(organization):
    try:
        return get_list_of_popular_products(organization).to_dict()
    except Exception as e:
        return str(e)


@app.route('/popular_categories/<organization>', methods=['GET'])
def get_popular_categories_algo(organization):
    try:
        return get_popular_categories(organization).to_dict()
    except Exception as e:
        return str(e)


@app.route('/get_pairs/<organization>', methods=['GET'])
def get_pairs_algo(organization):
    try:
        return get_pairs(organization)
    except Exception as e:
        return str(e)


@app.route('/get_predictions/<organization>', methods=['GET'])
def get_predictions_algo(organization):
    try:
        return get_predictions(organization)
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8020)
