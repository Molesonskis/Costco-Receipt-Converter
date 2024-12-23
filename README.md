# Costco Receipt Calculator

## Overview

The Costco Receipt Calculator is a simple Python-based application designed to streamline the process of calculating and generating simplified receipts for Costco purchases in the UK. It handles VAT calculations, discounts, and item quantities, providing a clear breakdown of costs for better transparency.

## Features

- **Item Entry**: Add items with details such as name, pre-tax price, VAT rate, quantity, and discount per unit.
- **VAT Calculation**: Automatically applies VAT based on the specified tax code (0%, 5%, or 20%).
- **Discount Handling**: Supports per-unit discounts that are correctly applied before VAT calculation.
- **Quantity Support**: Calculates total costs for multiple quantities of the same item.
- **Receipt Generation**: Displays a concise, formatted receipt with subtotals, VAT, discounts, and the grand total.

## Usage

### Run the Application

Execute the script using Python.

### Main Menu Options

- **Add Item**: Enter details for an item to add it to the receipt.
- **Print Receipt**: Generate and display the full receipt.
- **Exit**: Quit the application.

### Data Input

- Enter the item name.
- Specify the pre-tax price.
- Enter the quantity.
- Choose the tax code (0 for 0%, 5 for 5%, 20 for 20%).
- Optionally, provide a discount per unit.

## Example

### Input

- Item Name: "Milk"
- Price: £1.20
- Quantity: 2
- Tax Code: 0
- Discount per Unit: £0.10

### Output

--- Simplified Receipt ---
Item: Milk
  Price: £1.20 x 2
  VAT (0%): £0.00
  Discount per unit: £0.10
  Total: £2.20

--- Totals ---
Subtotal (without VAT): £2.20
Total VAT: £0.00
Total Discounts: £0.20
Grand Total: £2.20

## VAT Rates

0%: Essential goods (e.g., food).

5%: Reduced-rate goods/services.

20%: Standard-rate goods/services.

## Requirements

Python 3.6+

## Future Improvements

- Add the ability to save receipts to a file.
- Enhance the interface with a GUI or web frontend.
- Support for multiple currencies and international tax rates.

## License

This project is free to use and modify.
