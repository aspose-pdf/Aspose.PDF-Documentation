---
title: Python での PDF ファイルのセキュリティ保護と署名
linktitle: PDF のセキュリティ保護と署名
type: docs
weight: 210
url: /ja/python-net/securing-and-signing/
description: デジタル署名、スマートカード、文書権限など、PythonでPDFファイルに署名、暗号化、復号化、保護する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF ドキュメントに署名、暗号化、復号化、保護を行う
Abstract: このセクションでは、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントを保護および署名する方法について説明します。Python でデジタル署名を適用する方法、スマートカードと証明書を使用する方法、署名情報を抽出する方法、PDF 暗号化、パスワード、アクセス権を管理する方法について説明します。
---

このセクションでは、Python Library を使用して PDF 文書にデジタル署名を安全に適用する方法について説明します。電子署名とデジタル署名という用語は同じ意味で使用されることもありますが、同じではありません。デジタル署名の裏付けとなるのは [認証局](https://en.wikipedia.org/wiki/Certificate_authority)、文書を改ざんから保護する信頼できるシールが付いています。これとは対照的に、電子署名は通常、同じレベルのセキュリティ検証を行わずに、文書に署名する意思を示すために使用されます。

これらのガイドは、Python ワークフローで PDF コンテンツの保護、文書権限の管理、信頼性の検証、証明書ベースの署名の適用などを行う必要がある場合にお使いください。

## 対象となるセキュリティタスクと署名タスク

Aspose.PDF はデジタル署名をサポートしています。

- RSA 署名アルゴリズムと SHA-1 ダイジェストを備えた PKCS1
- RSA 署名アルゴリズムと SHA-1 ダイジェストを備えた PKCS7
- PKCS7 は DSA、RSA、および ECDSA のシグネチャアルゴリズムを使用してデタッチされました。サポートされるダイジェストアルゴリズムは、署名アルゴリズムによって異なります。
- タイムスタンプ署名。

PKCS7のダイジェストアルゴリズムがデタッチされました:

- DSA-SHA-1。
- RSA-SHA-1、SHA-256、SHA-384、SHA-512。
- ECDSA-SHA-256、SHA-384、SHA-512、SHA3-256、SHA3-384、SHA3-512。

SHA-1ダイジェストアルゴリズムは安全ではないため、デジタル署名は避けることをお勧めします。

- [PDF ファイルにデジタル署名](/pdf/ja/python-net/digitally-sign-pdf-file/)
- [権限の設定、PDF ファイルの暗号化と復号化](/pdf/ja/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [画像および署名情報の抽出](/pdf/ja/python-net/extract-image-and-signature-information/)
- [スマートカードから PDF ドキュメントに署名](/pdf/ja/python-net/sign-pdf-document-from-smart-card/)
