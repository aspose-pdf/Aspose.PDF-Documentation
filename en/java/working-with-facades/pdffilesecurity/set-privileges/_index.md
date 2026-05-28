---
title: Set Privileges on an Existing PDF File
linktitle: Set Privileges on an Existing PDF File
type: docs
weight: 40
url: /java/set-privileges/
description: Learn how to set PDF document privileges in Java with PdfFileSecurity, with or without passwords.
lastmod: "2026-05-28"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Set PDF privileges in Java with PdfFileSecurity
Abstract: This article explains how to use the privilege-setting examples from `PdfFileSecurityExamples` in Aspose.PDF for Java. The current Java source includes applying privileges without passwords, applying privileges with user and owner passwords, and a boolean-returning privilege workflow for failure-aware handling.
---
The current Java source provides three privilege examples:

- `setPdfPrivilegesWithoutPasswords`, which creates a restricted `DocumentPrivilege`, re-enables printing, and applies it with `setPrivilege(privilege)`
- `setPdfPrivilegesWithPasswords`, which applies privileges through `setPrivilege("user_password", "owner_password", privilege)`
- `trySetPdfPrivilegesWithoutException`, which uses `trySetPrivilege(...)` and only saves the output when the privilege update succeeds

These examples show how to configure a `DocumentPrivilege` object and then apply it either directly or together with explicit passwords.
