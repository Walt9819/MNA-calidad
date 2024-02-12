"""
This script computes the total cost of all sales given a price catalogue
and a sales record.
"""
import sys
import json
import time


def load_json_file(filename):
    """
    Load a JSON file and return its contents as a dictionary.
    If an error occurs, return None.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    # Catch if the file does not exist or is not a valid JSON file
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading {filename}: {str(e)}")
        return None


def compute_total_sales(prices, sales):
    """
    Compute the total cost of all sales given a dictionary of prices
    and a list of sales.
    """
    total_cost = 0
    for sale in sales:
        product_id = sale.get('Product')
        quantity = sale.get('Quantity', 0)
        product_price = prices.get(product_id, 0)
        total_cost += product_price * quantity
    return total_cost


def main(price_catalogue_file, sales_record_file):
    """
    Main function to compute the total cost of all sales
    and print the results.
    """
    start_time = time.time()
    # Load JSON data
    prices = load_json_file(price_catalogue_file)
    sales = load_json_file(sales_record_file)
    if prices is None or sales is None:
        return
    # Convert prices to a dictionary for easier access
    price_dict = {item['title']: item['price'] for item in prices}
    # Compute total sales
    total_cost = compute_total_sales(price_dict, sales)
    # Print and save results
    result_string = f"Total cost of all sales: {total_cost}\n"
    execution_time = time.time() - start_time
    result_string += f"Execution time: {execution_time} seconds"
    print(result_string)
    with open('SalesResults.txt', 'w', encoding='utf-8') as result_file:
        result_file.write(result_string)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("""
              Usage: python compute_sales.py price_
              catalogue.json sales_record.json""")
    else:
        main(sys.argv[1], sys.argv[2])
