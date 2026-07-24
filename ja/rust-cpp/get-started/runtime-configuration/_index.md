---
title: ランタイム構成 Aspose.PDF for Rust via C++
linktitle: ランタイム構成
type: docs
weight: 100
url: /ja/rust-cpp/runtime-configuration/
description: Aspose.PDF のようなネイティブ動的ライブラリに依存する Rust アプリケーションは、Linux および macOS システムで正しく機能するために、正しいランタイムパス構成が必要です
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rust 用ネイティブ Aspose.PDF の RPATH 設定
Abstract: Rustでネイティブ動的ライブラリを使用する際、適切なランタイムリンクはアプリケーションが必要な依存関係を見つけられるようにするために不可欠です。Linux と macOS では、RPATH が明示的に設定されていない限り、システムの動的ローダーは実行ファイルのディレクトリを自動的に検索しません。本記事では、Rust アプリケーションが実行時に Aspose.PDF のネイティブライブラリを正しく検出できるように RPATH を設定する方法を解説します。Cargo を使用したプロジェクトレベルの設定、RUSTFLAGS を用いた環境ベースの設定、システム全体へのインストールオプション、そして Windows の動作に関する注意点について取り上げます。
SoftwareApplication: rust-cpp
---

> Rustでネイティブ動的ライブラリを使用する際の標準的な要件です。

Linux と macOS では、システムの動的ローダは RPATH が設定されていない限り、実行ファイルのディレクトリを自動的に検索しません。実行時にアプリケーションが Aspose.PDF のネイティブライブラリを見つけられるようにするには、**RPATH**（Run-time Search Path）を設定する必要があります。

当社のビルドスクリプトはライブラリを抽出し、出力ディレクトリにそれへのシンボリックリンクを作成しようとします (e.g., `target/debug/`）。 実行可能ファイルが見つかるようにするには、次のいずれかのオプションを選択してください:

## オプション 1: プロジェクトレベルの構成（推奨）

名前付きフォルダーを作成する `.cargo` プロジェクトのルートディレクトリに（存在しない場合は）作成し、ファイル名を付けます `config.toml` 内部に：

```toml
[target.'cfg(target_os = "linux")']
rustflags = ["-C", "link-arg=-Wl,-rpath,$ORIGIN"]

[target.'cfg(target_os = "macos")']
rustflags = ["-C", "link-arg=-Wl,-rpath,@loader_path"]
```

## オプション 2: RUSTFLAGS 環境変数

以下のフラグを使用してプロジェクトをビルドします:

```bash
# Linux
RUSTFLAGS="-C link-arg=-Wl,-rpath,\$ORIGIN" cargo build

# macOS
RUSTFLAGS="-C link-arg=-Wl,-rpath,@loader_path" cargo build
```

## オプション3: システム全体へのインストール（開発時には推奨されません）

ライブラリをグローバルにインストールする場合は、次のようにします：

* **Linux:** コピー `.so` ファイルへ `/usr/local/lib` そして実行 `sudo ldconfig`.
* **macOS:** コピーする `.dylib` ファイルへ `/usr/local/lib`.

> **Windows**
> 通常、ライブラリが同じフォルダーにあるため、特別な操作は必要ありません。 `.exe`. あるいは、対象のディレクトリを追加することもできます。 `.dll` あなたのシステムへ `PATH` 環境変数。