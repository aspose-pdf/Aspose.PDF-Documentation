---
title: GoでPDFの保護と署名
linktitle: PDFの保護と署名
type: docs
weight: 50
url: /ja/go-cpp/securing-and-signing/
description: このセクションでは、Goを使用して署名を利用し、PDFドキュメントを保護する機能について説明します
lastmod: "2026-07-04"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

このセクションでは、C++経由で Aspose.PDF for Go を使用して保護された PDF ドキュメントを扱うための包括的なガイドを提供します。PDF ファイルをパスワードで保護し、アクセス権限を管理し、Go アプリケーションで暗号化されたドキュメントを安全に開いたり解除したりする方法を説明します

この記事では、最新の暗号アルゴリズムを使用した PDF の暗号化、パスワードで保護されたファイルの復号、権限フラグによるユーザーアクセスの制御など、一般的なセキュリティ関連の PDF タスクを順に解説します。また、既存の権限設定を確認し、所有者の資格情報を使用して保護されたドキュメントを開き、さらに処理する方法も学べます

PDF ドキュメントの作成方法、AES ベースの暗号化を使用した最新の暗号保護の適用方法、印刷やコンテンツ編集、フォーム入力などのユーザー機能の制御方法を学びます。この記事では、所有者の資格情報を使用してパスワード保護された PDF を開き、復号してさらなる処理に適した制限のないドキュメントを作成する方法も示しています

- [PDF ファイルを暗号化](/pdf/ja/go-cpp/encrypt-pdf/)
- [PDF ファイルを復号化](/pdf/ja/go-cpp/decrypt-pdf/)
- [権限を取得](/pdf/ja/go-cpp/get-permissions/)
- [権限を設定](/pdf/ja/go-cpp/set_permissions/)
- [パスワードで保護された PDF を開く](/pdf/ja/go-cpp/open-password-protected-pdf/)

Set Permissions と Get Permissions の手順については、PDF Permissions Reference テーブルをご参照ください。このテーブルには、エンドユーザーの操作を制御するために PDF ドキュメントに適用できる利用可能な権限フラグが一覧表示されています。

## PDF 権限リファレンス

| **権限** | **説明** |
| :- | :- |
| PrintDocument | 印刷を許可 |
| ModifyContent | コンテンツの変更を許可（フォーム/注釈を除く） |
| ExtractContent | テキストと画像のコピー/抽出を許可 |
| ModifyTextAnnotations | テキスト注釈の追加/変更を許可 |
| FillForm | インタラクティブフォームの入力を許可する |
| ExtractContentWithDisabilities | アクセシビリティのためのコンテンツ抽出を許可する |
| AssembleDocument | ページの挿入/回転/削除や構造の変更を許可する |
| PrintingQuality | 高品質／忠実な印刷を許可 |
