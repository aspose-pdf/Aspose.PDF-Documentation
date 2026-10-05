---
title: Java を使用して PDF ヘッダーとフッターを管理する
linktitle: PDF のヘッダーとフッターを管理する
type: docs
weight: 70
url: /ja/java/artifacts-header-footer/
description: Aspose.PDF for Java を使用して PDF ドキュメントにヘッダーおよびフッターのアーティファクトを追加および削除する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java を使用して PDF ヘッダーとフッターを追加、カスタマイズ、削除する方法
Abstract: このガイドでは、Aspose.PDF for Java を使用して PDF ドキュメント内のヘッダーおよびフッターアーティファクトを管理する方法を説明します。再利用可能な `HeaderArtifact` および `FooterArtifact` オブジェクトをカスタムテキストステートと配置で作成し、ページに追加し、既存のヘッダーおよびフッターアーティファクトを削除する方法を取り上げます。
---
ヘッダーとフッターのアーティファクトは、繰り返しラベルやページ識別子、レイアウトフレーミングなどに一般的に使用される、コンテンツではないページネーション要素です。

## ヘッダーアーティファクトの作成

一貫したテキストスタイリングと配置を持つ再利用可能なヘッダーアーティファクトが必要な場合に、このヘルパーを使用してください。

1. [HeaderArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerartifact/)を作成してください。
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

## フッターアーティファクトの作成

このヘルパーは、ヘッダーアーティファクトと同じスタイリングパターンを持つ再利用可能なフッターアーティファクトを作成します。

1. [FooterArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/footerartifact/)を作成してください。
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

## ヘッダーアーティファクトの追加

ページに再利用可能なヘッダーアーティファクトを表示する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ヘルパーメソッドを通じてヘッダーアーティファクトを作成してください。
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

## フッター アーティファクトの追加

ページが再利用可能なフォーマットでフッターアーティファクトを表示する場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ヘルパーメソッドを使用してフッターアーティファクトを作成してください。
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

## ヘッダーとフッターのアーティファクトの削除

既存のヘッダーおよびフッターのアーティファクトをページから削除する必要がある場合に、この方法を使用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ページのアーティファクトコレクションを逆順に反復処理してください。
1. サブタイプがヘッダーまたはフッターであるページネーションアーティファクトを削除し、ドキュメントを保存してください。

```java
public static void deleteHeaderFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && (artifact.getSubtype() == Artifact.ArtifactSubtype.Header
                    || artifact.getSubtype() == Artifact.ArtifactSubtype.Footer)) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```
