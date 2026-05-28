---
title: Change Password of PDF File
linktitle: Change Password of PDF File
type: docs
weight: 10
url: /java/change-password/
description: Learn how to change PDF user and owner passwords in Java with PdfFileSecurity.
lastmod: "2026-05-28"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Change PDF passwords in Java with PdfFileSecurity
Abstract: This article explains how to use the password-change examples from `PdfFileSecurityExamples` in Aspose.PDF for Java. The current Java source includes changing both user and owner passwords, changing passwords while resetting privilege settings and key size, and a boolean-returning password-change workflow for failure-aware handling.
---
The current Java source provides three password-change examples:

- `changeUserAndOwnerPassword`, which updates both passwords with `changePassword(owner, newUser, newOwner)`
- `changePasswordAndResetSecurity`, which uses the overload that also applies a new `DocumentPrivilege` object and `KeySize.x128`
- `tryChangePasswordWithoutException`, which calls `tryChangePassword(...)` and only saves the result if the operation succeeds

These examples show both the basic password replacement flow and the overload that resets security settings while updating credentials.
