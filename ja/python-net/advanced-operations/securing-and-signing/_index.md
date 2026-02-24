---
title: PythonでPDFを保護および署名する
linktitle: PDFの保護と署名
type: docs
weight: 210
url: /ja/python-net/securing-and-signing/
description: このセクションでは、Pythonを使用して署名を利用し、PDF文書を保護する機能について説明します。
lastmod: "2025-06-23"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PythonでPDF文書に署名する
Abstract: この Aspose.PDF for Python via .NET ドキュメントのセクションは、プログラムでPDF文書を保護および署名するための包括的なガイドを提供します。パスワード保護、暗号化アルゴリズム、デジタル署名の適用と検証、証明書の取り扱い、文書の権限設定などの重要なトピックをカバーしています。開発者は、機密コンテンツを保護し、文書の完全性を保証し、規制基準に準拠するためのさまざまなセキュリティレベルの実装方法を学びます。例と API リファレンスにより、セキュリティ機能を Python アプリケーションに迅速に統合でき、PDF ワークフローを安心して保護できます。
---

このセクションでは、Python ライブラリを使用して PDF 文書にデジタル署名を安全に適用する方法を説明します。電子署名とデジタル署名という用語は時折同義に使われますが、同じものではありません。デジタル署名は [証明機関](https://en.wikipedia.org/wiki/Certificate_authority) によって裏付けられ、文書の改ざんから保護する信頼できるシールを提供します。対照的に、電子署名は通常、文書に署名する意思を示すために使用され、同等のセキュリティ検証は行われません。

Aspose.PDFはデジタル署名をサポートしています:

- RSA署名アルゴリズムとSHA-1ダイジェストを使用したPKCS1。
- RSA署名アルゴリズムとSHA-1ダイジェストを使用したPKCS7。
- DSA、RSA、ECDSA署名アルゴリズムを使用したPKCS7デタッチド。サポートされるダイジェストアルゴリズムは署名アルゴリズムに依存します。
- タイムスタンプ署名。

PKCS7デタッチドのダイジェストアルゴリズム：

- DSA - SHA-1。
- RSA - SHA-1、SHA-256、SHA-384、SHA-512。
- ECDSA - SHA-256、SHA-384、SHA-512、SHA3-256、SHA3-384、SHA3-512。

安全性の低さから、SHA-1ダイジェストアルゴリズムを使用したデジタル署名は避けることが推奨されます。

- [PDFファイルにデジタル署名](/pdf/python-net/digitally-sign-pdf-file/)
- [権限設定、暗号化および復号化PDFファイル](/pdf/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [画像と署名情報の抽出](/pdf/python-net/extract-image-and-signature-information/)
- [スマートカードからPDF文書に署名](/pdf/python-net/sign-pdf-document-from-smart-card/)
