---
title: システム要件
linktitle: システム要件
type: docs
weight: 30
url: /ja/python-net/system-requirements/
description: このセクションでは、開発者が Aspose.PDF for Python を正常に使用するために必要なサポート対象オペレーティングシステムを一覧表示します。
lastmod: "2025-02-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Python via .NET のサポート対象オペレーティングシステム
Abstract: Aspose.PDF for Python via .NET は、Microsoft Office や Adobe Acrobat Automation を必要とせずに PDF ドキュメントを管理できるように設計された PDF 処理 API です。Python 3.5 以降がインストールされた Windows や Linux など、さまざまなオペレーティングシステム上で 32 ビットおよび 64 ビットの Python アプリケーションの開発をサポートします。API は Windows XP から Windows 11 までの複数の Windows バージョン、Ubuntu、OpenSUSE、CentOS といった主要な Linux ディストリビューションと互換性があります。Linux システムの場合、特定の要件として GCC-6 ランタイムライブラリ、.NET Core Runtime の依存関係（Runtime 自体のインストールは不要）、Python 3.5-3.7 用の pymalloc ビルドが必要です。また、共有 libpython ライブラリが必要となり、正しいライブラリパスを認識させるために設定の調整が必要になる場合があります。
---

## 概要

Aspose.PDF for Python via .NET は、Microsoft Office® や Adobe Acrobat Automation を必要とせずに PDF ドキュメントを操作できる PDF 処理 APIです。Aspose.PDF for Python は、Python 3.5 以降がインストールされている Windows や Linux などのさまざまなオペレーティングシステム向けに、32 ビットおよび 64 ビットの Python アプリケーションを開発するために使用できます。

## サポート対象オペレーティングシステム

### Windows

- Windows 2003 Server
- Windows 2008 Server
- Windows 2012 Server
- Windows 2012 R2 Server
- Windows 2016 Server
- Windows 2019 Server
- Windows XP
- Windows Vista
- Windows 7
- Windows 8, 8.1
- Windows 10
- Windows 11

### Linux

- Ubuntu
- OpenSUSE
- CentOS
- その他

## 対象 Linux のシステム要件

- GCC-6 ランタイムライブラリ（またはそれ以降）。

- .NET Core Runtime の依存関係。 .NET Core Runtime 自体のインストールは不要です。

- Python 3.5-3.7 用: Python の pymalloc ビルドが必要です。--with-pymalloc Python ビルドオプションはデフォルトで有効になっています。通常、pymalloc ビルドの Python はファイル名に m サフィックスが付いています。

- libpython 共有 Python ライブラリ。--enable-shared Python ビルドオプションはデフォルトで無効になっており、一部の Python ディストリビューションには libpython 共有ライブラリが含まれていません。一部の Linux プラットフォームでは、パッケージマネージャを使用して libpython 共有ライブラリをインストールできます（例: sudo apt-get install libpython3.7）。一般的な問題は、libpython ライブラリが標準の共有ライブラリ用システムパスとは異なる場所にインストールされることです。この問題は、Python をコンパイルする際にビルドオプションで代替ライブラリパスを設定するか、システムの標準共有ライブラリディレクトリに libpython ライブラリファイルへのシンボリックリンクを作成することで解決できます。通常、libpython 共有ライブラリのファイル名は Python 3.5-3.7 の場合 libpythonX.Ym.so.1.0、Python 3.8 以降の場合 libpythonX.Y.so.1.0 です（例: libpython3.7m.so.1.0、libpython3.9.so.1.0）。



