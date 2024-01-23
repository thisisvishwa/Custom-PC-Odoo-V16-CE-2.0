# Custom PC Building Module - Administrator Guide

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Managing Product Categories](#managing-product-categories)
5. [Real-time Price and Availability Setup](#real-time-price-and-availability-setup)
6. [Budget Management](#budget-management)
7. [Build Validation and Compatibility Checks](#build-validation-and-compatibility-checks)
8. [Order Generation and Processing](#order-generation-and-processing)
9. [Reporting and Analytics](#reporting-and-analytics)
10. [Security Measures](#security-measures)
11. [Troubleshooting](#troubleshooting)
12. [Changelog](#changelog)

## Introduction

This guide is intended for administrators of the Odoo 16 Community Edition who wish to install and configure the Custom PC Building Module. This module allows users to configure and order custom PCs through both the backend and the eCommerce website.

## Installation

Refer to the [installation_guide.md](installation_guide.md) for detailed instructions on how to install the Custom PC Building Module.

## Configuration

After installation, access the Odoo backend and navigate to the Custom PC module settings. Here you can configure the following:

- Set the `CUSTOM_PC_CATEGORY_ID` to integrate the "Custom PCs" product category.
- Configure API credentials for real-time price and availability updates.

## Managing Product Categories

To manage product categories:

1. Go to Inventory > Configuration > Product Categories.
2. Add or edit the "Custom PCs" category using the `CUSTOM_PC_CATEGORY_ID`.

## Real-time Price and Availability Setup

To set up real-time price and availability:

1. Navigate to Custom PC > Configuration.
2. Enter the API credentials for the vendors you wish to integrate.
3. Use the `ExternalAPIIntegration` class to test the connection.

## Budget Management

For budget management:

1. Go to the Custom PC module settings.
2. Configure the `BUDGET_LIMIT_KEY` to set default budget limits.

## Build Validation and Compatibility Checks

To manage build validation and compatibility checks:

1. Access the Custom PC module settings.
2. Configure the `BuildValidator` and `CompatibilityChecker` utilities.
3. Set up rules for component validation and compatibility checks.

## Order Generation and Processing

To handle order generation:

1. Ensure the module is integrated with the Sales module.
2. Use the `generateOrder()` function to create detailed order lists from configured PC builds.

## Reporting and Analytics

To access reporting and analytics:

1. Navigate to Custom PC > Reporting.
2. Use the provided tools to analyze trends and user preferences.

## Security Measures

Ensure the following security measures are in place:

- Use `ENCRYPT_CUSTOMER_DETAILS` and `VALIDATE_PAYMENT_INFO` to secure customer and payment information.
- Regularly review and update security protocols.

## Troubleshooting

For common issues:

- Refer to the error logs in the Odoo backend.
- Check the `test_custom_pc.py` file for automated tests that can help identify problems.

## Changelog

For a detailed list of changes, refer to the [changelog.md](changelog.md) file.