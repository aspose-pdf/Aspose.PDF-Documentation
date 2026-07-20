---
title: Aspose.PDF for Rust via C++ のインストール方法
linktitle: インストール
type: docs
weight: 20
url: /ja/rust-cpp/installation/
description: このセクションでは、製品の説明と、Aspose.PDF for Rust を自分でインストールする手順を示します。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Rust のインストールガイド
Abstract: Aspose.PDF for Rust via C++ インストールガイドは、Rust プロジェクトで C++ 統合を使用するためにライブラリをインストールおよび構成する手順を段階的に提供します。手動セットアップや NuGet のようなパッケージマネージャーの使用など、さまざまなインストール方法をカバーしています。ガイドでは、システム要件、依存関係、および開発環境へのシームレスな統合を確保するために必要な構成手順も概説しています。このドキュメントは、開発者が Rust を介した C++ で PDF ドキュメントの作成、読み取り、操作を効果的に開始できるよう支援します。
SoftwareApplication: rust-cpp
---

## インストール

### Aspose のウェブサイトからのインストール

このパッケージには、大きなファイルが含まれており、bzip2 アーカイブとして保存されています。

1. **ダウンロード** アーカイブ **Aspose.PDF for Rust via C++** を公式Asposeウェブサイトから。
   最新（最も最近の）バージョンは上部に表示され、**Download** ボタンをクリックするとデフォルトでダウンロードされます。
   この最新版の使用が推奨されます。必要な場合のみ、以前のバージョンをダウンロードしてください。
   例: `Aspose.PDF-for-Rust-via-CPP-25.6.zip`

   アーカイブのファイル名形式は: `Aspose.PDF-for-Rust-via-CPP-YY.M.zip`、どこ:
   - `YY` = 年の下二桁 (例、 `25` 2025年用)
   - `M` = 月の番号から `1` へ `12`

2. **抽出** アーカイブを選択したディレクトリに `{path}` 適切なツールを使用して:

   - Linux/macOS 上で:

     ```bash
     unzip Aspose.PDF-for-Rust-via-CPP-YY.M.zip -d {path}
     ```

   - Windowsでは、組み込みのエクスプローラ抽出機能または任意の解凍ツール（7-Zip、WinRAR）を使用してください。

3. **Add** ライブラリを Rust プロジェクトの依存関係として追加します。これを行う方法は 2 つあります:

   - **コマンドラインを使用する:**

     ```bash
     cargo add asposepdf --path {path}/asposepdf
     ```

   - **手動で編集** `Cargo.toml`:**
     プロジェクトを開く `Cargo.toml` 以下を追加してください `[dependencies]`:

     ```toml
     [dependencies]
     asposepdf = { path = "{path}/asposepdf" }
     ```

4. **プロジェクトをビルドする** (`cargo build`). 最初のビルド時に、プラットフォームに適した動的ライブラリが自動的に抽出されます。 `.bz2` アーカイブ内の `lib` フォルダーがプロジェクトにリンクされています。

**注記**

- ビルドスクリプトは、出力ディレクトリ内のライブラリへの**シンボリックリンク**の作成を試みます（例、 `target/debug/`).
- **Linux と macOS** 用に、次のことも実行する必要があります [ランタイム構成](#runtime-configuration) 以下のセクションは、実行時に実行可能ファイルがライブラリを見つけられるようにするためのものです。
- すべて `.bz2` アーカイブには対応するものがあります `.sha256` チェックサムファイル。チェックサムが欠落しているか無効な場合、ビルドは失敗します。

### GitHubからのインストール

このパッケージには、事前にコンパイルされたネイティブライブラリが含まれています（`.dll`, `.so`, `.dylib`） が圧縮された状態で保存されます `.bz2` GitHub リポジトリ内のアーカイブ。

1. **Add** ライブラリを Rust プロジェクトの依存関係として追加します。これを行う方法は 2 つあります:

   - **コマンドラインを使用する:**

     ```bash
     cargo add asposepdf --git https://github.com/aspose-pdf/aspose-pdf-rust-cpp.git
     ```

   - **手動で編集** `Cargo.toml`:**

     プロジェクトを開く `Cargo.toml` 以下を追加してください `[dependencies]`:

     ```toml
     [dependencies]
     asposepdf = { git = "https://github.com/aspose-pdf/aspose-pdf-rust-cpp.git" }
     ```

    > **注:** 特定のリリースバージョンを使用するには、タグを指定できます。
    >
    > ```toml
    > asposepdf = { git = "https://github.com/aspose-pdf/aspose-pdf-rust-cpp.git", tag = "v1.26.1" }
    > ```

2. **プロジェクトをビルドする** (`cargo build`). 最初のビルド時に、プラットフォームに適した動的ライブラリが自動的に抽出されます。 `.bz2` アーカイブ内の `lib` フォルダーがプロジェクトにリンクされています。

**注記**

- ファイルを手動でダウンロードしたり抽出したりする必要はありません - すべてはGitHubリポジトリに含まれています。
- ビルドスクリプトは、出力ディレクトリ内のライブラリへの**シンボリックリンク**の作成を試みます（例、 `target/debug/`).
- **Linux と macOS** 用に、次のことも実行する必要があります [ランタイム構成](#runtime-configuration) 以下のセクションは、実行時に実行可能ファイルがライブラリを見つけられるようにするためのものです。
- すべて `.bz2` アーカイブが一致しています `.sha256` チェックサムファイル。チェックサムは展開前に検証されます。
- チェックサムの検証が失敗するか、アーカイブが存在しない場合、ビルドは詳細なエラーとともに失敗します。

### crates.io からのインストール

このパッケージは利用可能です [crates.io](https://crates.io/crates/asposepdf). 
サイズ制限のため、公開されたクレートにはネイティブ バイナリ ライブラリが含まれていません (`.dll`, `.so`, または `.dylib`).
必要なネイティブライブラリは、公式配布アーカイブ（参照）から取得できます。 [Aspose のウェブサイトからのインストール](#installation-from-aspose-website)）またはGitHubリポジトリから（参照 [GitHubからのインストール](#installation-from-github)).
ビルド スクリプトは、ビルド プロセス中に圧縮された .bz2 アーカイブから適切なネイティブ ライブラリを検索し、検証し、抽出します。

1. **Add** ライブラリを Rust プロジェクトの依存関係として追加します。これを行う方法は 2 つあります:

   - **コマンドラインを使用する:**

     ```bash
     cargo add asposepdf
     ```

   - **手動で編集** `Cargo.toml`:**

     プロジェクトを開く `Cargo.toml` 以下を追加してください `[dependencies]`:

     ```toml
     [dependencies]
     asposepdf = "1.26.1"
     ```

2. **パスを設定**: ネイティブ ライブラリが含まれるディレクトリに設定し、必要なファイルをダウンロードしてください。

   - **環境変数を設定する** `ASPOSE_PDF_LIB_DIR`** ネイティブを配置するフォルダーを指すように `.bz2` アーカイブ、彼らの `.sha256` チェックサムファイル、抽出されたネイティブライブラリ（`.dll`, `.so`, `.dylib`、そして Windows でも `.lib`):

     - Linux/macOS の場合:

       ```bash
       export ASPOSE_PDF_LIB_DIR=/path/to/lib
       ```

     - Windows (コマンド プロンプト)の場合:

       ```cmd
       set ASPOSE_PDF_LIB_DIR=C:\path\to\lib
       ```

     - Windows (PowerShell) の場合:
     
       ```powershell
       $env:ASPOSE_PDF_LIB_DIR = "C:\path\to\lib"
       ```

**ASPOSE_PDF_LIB_DIR に関する注意**

その `ASPOSE_PDF_LIB_DIR` environment variable はビルドスクリプトの作業ディレクトリを定義します。 この変数は **コンパイル中のみ** 使用され、ネイティブライブラリのアーカイブを検索、検証、抽出します。 この変数を設定しても、ディレクトリがシステムの実行時ライブラリ検索パスに自動的に追加されることは **ありません** (see [ランタイム構成](#runtime-configuration)).

  - **必要なものをダウンロード** `.bz2` GitHub リポジトリのアーカイブ** とチェックサムファイル [`lib/` フォルダー](https://github.com/aspose-pdf/aspose-pdf-rust-cpp/tree/main/lib) そして **それらを** 設定されたフォルダーに入れます `ASPOSE_PDF_LIB_DIR`:

  - **Linux x64** 用に、ダウンロード:
    - `libAsposePDFforRust_linux_amd64.so.bz2`
    - `libAsposePDFforRust_linux_amd64.so.bz2.sha256`

  - **macOS x86_64** 用に、ダウンロード：
    - `libAsposePDFforRust_darwin_amd64.dylib.bz2`
    - `libAsposePDFforRust_darwin_amd64.dylib.bz2.sha256`

  - **macOS arm64** 用に、ダウンロード:
    - `libAsposePDFforRust_darwin_arm64.dylib.bz2`
    - `libAsposePDFforRust_darwin_arm64.dylib.bz2.sha256`

  - **Windows x64** 用に、ダウンロード:
    - `AsposePDFforRust_windows_amd64.dll.bz2`
    - `AsposePDFforRust_windows_amd64.dll.bz2.sha256`
    - `AsposePDFforRust_windows_amd64.lib` (ネイティブインポートライブラリ、圧縮されていません)

**Note:** これらのファイルは GitHub から手動でダウンロードし、指示されたディレクトリに配置する必要があります。 `ASPOSE_PDF_LIB_DIR`.  
ビルドスクリプトは、ネイティブライブラリを自動的にアンパックします。 `.bz2` 最初のビルド時のアーカイブ。

3. **ビルド** あなたのプロジェクト (`cargo build`). 最初のビルド時に、プラットフォームに一致するネイティブ ライブラリが自動的に抽出されます `.bz2` アーカイブされ、プロジェクトにリンクされています。

**重要:** **Linux と macOS** の場合、以下も従う必要があります [ランタイム構成](#runtime-configuration) 以下のセクションは、実行時に実行可能ファイルがライブラリを見つけられるようにするためのものです。

**注記**

- その `ASPOSE_PDF_LIB_DIR` 変数は **ビルドプロセス中のみ** アーカイブを検索し抽出するために使用されます。
- ビルド スクリプトは、抽出されたライブラリへの **シンボリックリンク** を出力ディレクトリに作成しようとします (例として、 `target/debug/`).
- フォルダーを提供する必要があります `.bz2` そして `.sha256` ファイルは別々に、これらのバイナリアーカイブは crates.io を通じて配布されていません。
- 必要なアーカイブが存在しないか、チェックサムが失敗した場合、ビルドは詳細なエラーとともに失敗します。
- GitHub または Aspose のウェブサイトからのインストールに使用された同じバイナリファイルは、ここでも再利用できます。

## クイックスタート

すべてのコードスニペットはこの中に含まれています [スニペット](https://onedrive.live.com/examples).