# Task 02: Web Application Security - SQL Injection (SQLi)

## Overview
This module demonstrates web application auditing and exploitation using Burp Suite Community Edition as an intercepting proxy. It focuses on identifying and exploiting a SQL Injection vulnerability within an un-sanitized database filter.

## Repository Structure
- `exploits/sqli_payloads.txt`: Reference list of standard authentication and logic bypass SQLi payloads.
- `screenshots/`: Captured evidence of Burp Suite request interception and successful lab completion.

## Attack Methodology
1. **Traffic Interception:** Routed HTTP browser traffic through Burp Suite's embedded proxy listener.
2. **Parameter Manipulation:** Intercepted the category filter request (`GET /filter?category=...`) and appended the boolean payload `' OR 1=1--`.
3. **Database Logic Bypass:** The single quote (`'`) broke out of the string literal, `OR 1=1` evaluated to true for all rows, and `--` commented out the remaining SQL query parameters, dumping unreleased inventory.

## Vulnerability & Remediation

### The Vulnerable Query
```sql
-- Original vulnerable query constructed via raw string concatenation
SELECT * FROM products WHERE category = 'Gifts' AND released = 1;

-- Injected query executed by database
SELECT * FROM products WHERE category = '' OR 1=1--' AND released = 1;
