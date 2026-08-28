# TECHNICAL LAB REPORT: WEB APPLICATION SECURITY AUDIT
**Task 02:** SQL Injection (SQLi) Vulnerability Assessment & Exploitation  
**Date:** August 28, 2026  
**Target Application:** PortSwigger Web Security Academy – SQL Injection in WHERE Clause  
**Auditor:** Anita Nwokem  

---

## 1. Executive Summary
During a simulated web application security assessment, a critical SQL Injection (SQLi) vulnerability was identified within the target web store's category filtering mechanism. By manipulating client-side HTTP request parameters using Burp Suite Community Edition, an unauthenticated attacker can bypass database logic, view unreleased internal inventory, and dump restricted catalog records.

---

## 2. Technical Findings & Proof of Concept

### 2.1 Flaw Identification
The web application accepts user input via the `category` URL parameter in a `GET` request (`/filter?category=...`). The backend constructs database queries dynamically using string concatenation without proper input sanitization or parameter binding.

### 2.2 Attack Execution & Payload
1. **Interception:** Transmitted HTTP requests were intercepted via Burp Suite's proxy listener.
2. **Payload Construction:** The target URL parameter was modified by injecting a single quote (`'`) to break the SQL string literal, followed by a boolean condition (`OR 1=1`) and a comment sequence (`--`):
   ```http
   GET /filter?category=gifts%27+OR+1=1-- HTTP/1.1
   Host: target-app.web-security-academy.net
