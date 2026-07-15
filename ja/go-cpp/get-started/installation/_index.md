---
title: Aspose.PDF for Go via C++ のインストール方法
linktitle: インストール
type: docs
weight: 20
url: /ja/go-cpp/installation/
description: このセクションでは、製品の説明と Aspose.PDF for Go のインストール手順を自分で行う方法を示しています。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Go のインストールガイド
Abstract: Aspose.PDF for Go via C++ インストールガイドは、C++ 統合された Go プロジェクトでライブラリを使用するためのインストールと設定手順をステップバイステップで提供します。手動セットアップや NuGet などのパッケージマネージャーを使用するなど、さまざまなインストール方法をカバーしています。また、システム要件、依存関係、および開発環境へのシームレスな統合を確保するために必要な設定手順も概説しています。このドキュメントは、開発者が Go で C++ を介して PDF ドキュメントを作成、読み取り、操作することを効果的に始めるための助けとなります。
SoftwareApplication: go-cpp
---

## インストール

このパッケージには、bzip2 アーカイブとして保存されている大きなファイルが含まれています。

1. asposepdf パッケージをプロジェクトに追加します。

```sh
go get github.com/aspose-pdf/aspose-pdf-go-cpp@latest
```

2. 大きなファイルを生成する:

- **macOS と linux**

1. ターミナルを開く

2. Go モジュールキャッシュ内の github.com/aspose-pdf のフォルダーを一覧表示してください:

```sh
ls $(go env GOMODCACHE)/github.com/aspose-pdf/
```

3. 前のステップで取得したパッケージの特定バージョンフォルダーに現在のフォルダーを変更します：

```sh
cd $(go env GOMODCACHE)/github.com/aspose-pdf/aspose-pdf-go-cpp@vx.x.x
```

実際のパッケージ バージョンで `@vx.x.x` を置き換えてください。

4. スーパーユーザー権限で go generate を実行:

```sh
sudo go generate
```

- **ウィンドウズ**

1. コマンドプロンプトを開く

2. Go モジュールキャッシュ内の github.com/aspose-pdf のフォルダーを一覧表示してください:

```cmd
for /f "delims=" %G in ('go env GOMODCACHE') do for /d %a in ("%G\github.com\aspose-pdf\*") do echo %~fa
```

3. 前のステップで取得したパッケージの特定バージョンフォルダーに現在のフォルダーを変更します：

```cmd
cd <specific version folder of the package>
```

4. go generate を実行:

```cmd
go generate
```

5. パッケージの特定バージョンフォルダーを %PATH% 環境変数に追加します:

```cmd
setx PATH "%PATH%;<specific version folder of the package>\lib\"
```

置換 `<specific version folder of the package>` ステップ2で取得した実際のパスを使用して.

## テスト

ルートパッケージフォルダーからのテスト実行:

```sh
go test -v
```

## クイックスタート

すべてのコードスニペットは以下に含まれています [スニペット](https://github.com/aspose-pdf/aspose-pdf-go-cpp).
