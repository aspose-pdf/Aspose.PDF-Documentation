---
title: JavaでPDFヘッダーとフッターを追加する
linktitle: ヘッダーとフッターを追加する
type: docs
weight: 70
url: /ja/java/artifacts-header-footer/
description: スタイル付きのヘッダーとフッターのアーティファクトを作成し、JavaでPDFページに追加します。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaでヘッダーとフッターを追加する
Abstract: スタイル付きのヘッダーとフッターのアーティファクトを作成し、JavaでPDFページに追加します。
---
ヘッダーおよびフッターアーティファクトは、繰り返し使用されるラベル、ページ識別子、レイアウトのフレーミングに一般的に使用される、コンテンツではないページ付け要素です。

## ヘッダーアーティファクトを作成する

テキストのスタイリングと配置を一貫させた再利用可能なヘッダーアーティファクトが必要な場合に、このヘルパーを使用してください。

1. [HeaderArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerartifact/) オブジェクトを作成してください。
1. テキスト、フォント設定、前景色を設定してください。
1. 水平揃えを設定し、アーティファクトを返してください。

```java
public static HeaderArtifact createHeaderArtifact(String text) {
    HeaderArtifact artifact = new HeaderArtifact();
    artifact.setText(text);
    artifact.getTextState().setFontSize(14);
    artifact.getTextState().setFont(FontRepository.findFont("Arial"));
    artifact.getTextState().setForegroundColor(Color.getNavy());
    artifact.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
    return artifact;
}
```

## フッター アーティファクトを作成する

このヘルパーは、ヘッダー アーティファクトと同じスタイリング パターンを持つ再利用可能なフッター アーティファクトを作成します。

1. [FooterArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/footerartifact/) オブジェクトを作成してください。
1. テキスト、テキスト状態、および前景色を設定してください。
1. 配置を設定し、アーティファクトを返してください。

```java
public static FooterArtifact createFooterArtifact(String text) {
    FooterArtifact artifact = new FooterArtifact();
    artifact.setText(text);
    artifact.getTextState().setFontSize(14);
    artifact.getTextState().setFont(FontRepository.findFont("Arial"));
    artifact.getTextState().setForegroundColor(Color.getNavy());
    artifact.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
    return artifact;
}
```

## ヘッダー artifact を追加します

ページに再利用可能なヘッダーアーティファクトを表示する必要がある場合は、この例を使用してください。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) で元の PDF を開いてください。
1. ヘルパーメソッドを使用してヘッダーアーティファクトを作成してください。
1. アーティファクトをページに追加し、出力ファイルを保存してください。

```java
public static void addHeaderArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HeaderArtifact header = createHeaderArtifact("Sample Header");
        document.getPages().get_Item(1).getArtifacts().add(header);
        document.save(outputFile.toString());
    }
}
```

## フッターアーティファクトを追加

ページに再利用可能な書式設定を持つフッターアーティファクトを表示する必要がある場合は、この例を使用してください。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) で元の PDF を開いてください。
1. ヘルパーメソッドを介してフッターアーティファクトを作成してください。
1. アーティファクトをページに追加し、出力ファイルを保存してください。

```java
public static void addFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FooterArtifact footer = createFooterArtifact("Sample Footer");
        document.getPages().get_Item(1).getArtifacts().add(footer);
        document.save(outputFile.toString());
    }
}
```

## 関連トピック

- [ヘッダーとフッターを削除](/pdf/ja/java/remove-headers-footers/)
- [Java で PDF アーティファクトを操作](/pdf/ja/java/artifacts/)
