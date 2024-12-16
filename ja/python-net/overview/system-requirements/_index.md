---
title: システム要件
linktitle: システム要件
type: docs
weight: 30
url: /ja/python-net/system-requirements/
description: このセクションでは、Aspose.PDF for Python を正常に使用するために必要なサポートされているオペレーティングシステムを一覧表示します。
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 概要

Aspose.PDF for Python via .NETは、開発者がMicrosoft Office®やAdobe Acrobat Automationを必要とせずにPDFドキュメントを操作できるPDF処理APIです。Aspose.PDF for Pythonは、Python 3.5以降がインストールされている異なるオペレーティングシステム（WindowsやLinuxなど）向けに32ビットおよび64ビットのPythonアプリケーションの開発に使用できます。

## サポートされているオペレーティングシステム

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

## ターゲットLinuxのシステム要件

- GCC-6 ランタイムライブラリ（またはそれ以降）。

- .NET Core ランタイムの依存関係。.NET Core ランタイム自体のインストールは必要ありません。

- Python 3.5-3.7 の場合: Python の pymalloc ビルドが必要です。--with-pymalloc Python ビルドオプションはデフォルトで有効になっています。通常、Python の pymalloc ビルドはファイル名に m 接尾辞が付いています。

- libpython 共有ライブラリ。
 The --enable-shared Python build option はデフォルトで無効になっており、一部のPythonディストリビューションにはlibpython共有ライブラリが含まれていません。いくつかのLinuxプラットフォームでは、libpython共有ライブラリをパッケージマネージャーを使用してインストールできます。例えば: sudo apt-get install libpython3.7。一般的な問題は、libpythonライブラリが共有ライブラリの標準システム位置とは異なる場所にインストールされていることです。この問題は、Pythonをコンパイルする際に代替ライブラリパスを設定するPythonビルドオプションを使用して修正するか、共有ライブラリの標準システム位置にlibpythonライブラリファイルへのシンボリックリンクを作成することで修正できます。通常、libpython共有ライブラリファイル名はPython 3.5-3.7の場合libpythonX.Ym.so.1.0、Python 3.8以降の場合libpythonX.Y.so.1.0です（例: libpython3.7m.so.1.0、libpython3.9.so.1.0）。