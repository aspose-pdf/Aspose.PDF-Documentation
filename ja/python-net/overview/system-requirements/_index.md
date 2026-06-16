---
title: システム要件
linktitle: システム要件
type: docs
weight: 30
url: /ja/python-net/system-requirements/
description: このセクションでは、開発者が Aspose.PDF for Python を正常に使用するために必要な、サポート対象のオペレーティングシステムを一覧表示します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: .NET 経由で Python 用 Aspose.PDF がサポートされているオペレーティングシステム
Abstract: Aspose.PDF for Python via .NET は、開発者がマイクロソフトオフィスやアドビアクロバットオートメーションを必要とせずに PDF ドキュメントを管理できるように設計された PDF 処理 API です。Python 3.5 以降がインストールされている Windows や Linux など、さまざまなオペレーティングシステムでの 32 ビットおよび 64 ビットの Python アプリケーションの開発をサポートします。この API は、Windows XP から Windows 11 まで、いくつかの Windows バージョンと、Ubuntu、OpenSUSE、CentOS などの主要な Linux ディストリビューションと互換性があります。Linux システムの場合、GCC-6 ランタイムライブラリ、.NET Core ランタイムの依存関係 (ランタイム自体は不要です)、バージョン 3.5 ～ 3.7 の Python の pymalloc ビルドなどの特定の要件があります。さらに、共有の libpython ライブラリが必要なため、ライブラリパスを正しく認識できるように構成を調整する必要がある場合があります。
---

## 概要

.NET 経由の Aspose.PDF for Python、PDF 処理 API により、開発者はマイクロソフトオフィス® やアドビアクロバットオートメーションを必要とせずに PDF ドキュメントを操作できます。Aspose.PDF for Python を使用すると、Python 3.5 以降がインストールされているさまざまなオペレーティングシステム (Windows や Linux など) 用の 32 ビットおよび 64 ビットの Python アプリケーションを開発できます。

## サポート対象のオペレーティングシステム

### Windows

- ウィンドウズ 2003 サーバー
- ウィンドウズ 2008 サーバー
- ウィンドウズ 2012 サーバー
- ウィンドウズ 2012 R2 サーバー
- ウィンドウズ 2016 サーバー
- ウィンドウズ 2019 サーバー
- ウィンドウズ XP
- ウィンドウズビスタ
- ウィンドウズ 7
- ウィンドウズ 8、8.1
- ウィンドウズ 10
- ウィンドウズ 11

### リナックス

- ウブントゥ
- SUSE を開きます
- CentOS
- その他

## ターゲット Linux のシステム要件

- GCC-6 ランタイムライブラリ (またはそれ以降)

- .NET コアランタイムの依存関係。.NET Core ランタイム自体をインストールする必要はありません。

- Python 3.5-3.7 の場合:Python のピマロックビルドが必要です。--with-pymalloc Python ビルドオプションはデフォルトで有効になっています。通常、Python の pymalloc ビルドでは、ファイル名に m というサフィックスが付いています。

- libpython 共有の Python ライブラリ。--enable-shared Python ビルドオプションはデフォルトで無効になっています。一部の Python ディストリビューションには libpython 共有ライブラリが含まれていません。一部の Linux プラットフォームでは、sudo apt-get install libpython3.7 のように、パッケージマネージャーを使用して libpython 共有ライブラリをインストールできます。よくある問題は、libpython ライブラリーが、共有ライブラリーの標準的なシステム上の場所とは異なる場所にインストールされていることです。この問題は、Python のコンパイル時に Python ビルド・オプションを使用して代替ライブラリー・パスを設定することで解決できます。または、共有ライブラリーのシステム標準の場所にある libpython ライブラリー・ファイルへのシンボリック・リンクを作成することで問題を解決できます。通常、libpython 共有ライブラリのファイル名は Python 3.5-3.7 の場合は libPythonx.ym.so.1.0、Python 3.8 以降の場合は libPythonx.y.so.1.0 です (例:libpython3.7m.so.1.0、libpython3.9.so.1.0)。


