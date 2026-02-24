---
title: Python via .NET でアーティファクトを扱う
linktitle: アーティファクトの操作
type: docs
weight: 170
url: /ja/python-net/artifacts/
description: Aspose.PDF for Python via .NET を使用すると、PDF ページに背景画像を追加し、Artifact クラスを使用して各ウォーターマークを取得できます。
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF にアーティファクトを追加する
Abstract: この記事では、PDF 文書におけるアーティファクトの概念と応用について、特にアクセシビリティとパフォーマンス向上における役割に焦点を当てて解説します。アーティファクトは装飾やレイアウト要素など、文書の意味を伝えない非コンテンツ要素です。本稿では、Aspose.PDF for Python via .NET ライブラリの `Artifact` クラスを使用してこれらの要素を管理する方法を取り上げ、`custom_type`、`contents`、`opacity` などのプロパティによる詳細なカスタマイズを紹介します。また、特定のアーティファクトタイプを扱う関連クラスも紹介します。実践的な例として、ウォーターマークの取得、背景画像の追加、アーティファクトタイプのカウント、ベーツ番号付与の実装などの操作を示します。
---

PDF のアーティファクトは、文書の実際のコンテンツに含まれないグラフィックオブジェクトやその他の要素です。通常、装飾、レイアウト、背景目的で使用されます。アーティファクトの例として、ページヘッダー、フッター、区切り線、意味を持たない画像などがあります。

PDF におけるアーティファクトの目的は、コンテンツ要素と非コンテンツ要素を区別できるようにすることです。これはアクセシビリティにとって重要で、スクリーンリーダーやその他の支援技術がアーティファクトを無視し、関連するコンテンツに集中できるようになります。また、アーティファクトは印刷、検索、コピー時に除外できるため、PDF 文書のパフォーマンスと品質の向上にも寄与します。

PDF で要素をアーティファクトとして作成するには、[Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) クラスを使用する必要があります。
次の便利なプロパティが含まれています：

- **custom_type** - アーティファクトタイプの名前を取得します。標準でないタイプの場合に使用できます。
- **custom_subtype** - アーティファクトサブタイプの名前を取得します。標準サブタイプでない場合に使用できます。
- **type** - アーティファクトのタイプを取得します。
- **subtype** - アーティファクトのサブタイプを取得します。非標準サブタイプがある場合、サブタイプ名は CustomSubtype で取得できます。
- **contents** - アーティファクト内部オペレーターのコレクションを取得します。
- **form** - アーティファクトの XForm を取得します（XForm が使用されている場合）。
- **rectangle** - アーティファクトの矩形を取得します。
- **position** - アーティファクトの位置を取得または設定します。このプロパティが指定されている場合、余白と配置は無視されます。
- **right_margin** - アーティファクトの右余白。Position プロパティで位置が明示的に指定されている場合、この値は無視されます。
- **left_margin** - アーティファクトの左余白。Position プロパティで位置が明示的に指定されている場合、この値は無視されます。
- **top_margin** - アーティファクトの上余白。Position プロパティで位置が明示的に指定されている場合、この値は無視されます。
- **bottom_margin** - アーティファクトの下余白。Position プロパティで位置が明示的に指定されている場合、この値は無視されます。
- **artifact_horizontal_alignment** - アーティファクトの水平配置。Position プロパティで位置が明示的に指定されている場合、この値は無視されます。
- **artifact_vertical_alignment** - アーティファクトの垂直配置。Position プロパティで位置が明示的に指定されている場合、この値は無視されます。
- **rotation** - アーティファクトの回転角度を取得または設定します。
- **text** - アーティファクトのテキストを取得します。
- **image** - アーティファクトの画像を取得します（存在する場合）。
- **opacity** - アーティファクトの不透明度を取得または設定します。値は 0..1 の範囲です。
- **lines** - 複数行テキストアーティファクトの行。
- **text_state** - アーティファクトテキストのテキスト状態。
- **is_background** - true の場合、アーティファクトはページコンテンツの背後に配置されます。

以下のクラスもアーティファクトの作業に役立ちます：

- [ArtifactCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)
- [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)
- [ベーツ番号付け](https://reference.aspose.com/pdf/python-net/aspose.pdf/)

以下の記事セクションをご確認ください：

- [背景の追加](/pdf/python-net/add-backgrounds/) - Python で PDF ファイルに背景画像を追加します。
- [ベーツ番号付けの追加](/pdf/python-net/add-bates-numbering/) - PDF にベーツ番号付けを追加します。
- [ウォーターマークの追加](/pdf/python-net/add-watermarks/) - Python で PDF にウォーターマークを追加する方法です。
- [アーティファクトのカウント](/pdf/python-net/counting-artifacts/) - Python を使用して PDF のアーティファクトをカウントします。

