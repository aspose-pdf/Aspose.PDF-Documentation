---
title: PDFからサムネイル画像を生成する
linktitle: PDFからサムネイル画像を生成する
type: docs
weight: 110
url: ja/net/generate-thumbnail-images-from-pdf-documents/
description: このセクションでは、PDFドキュメントからサムネイル画像を生成する方法について説明します
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFからサムネイル画像を生成する",
    "alternativeHeadline": "PDFファイルからサムネイル画像を生成する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, サムネイル画像を生成する",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/generate-thumbnail-images-from-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/generate-thumbnail-images-from-pdf-documents/"
    },
    "dateModified": "2022-02-04",
    "description": "このセクションでは、PDFドキュメントからサムネイル画像を生成する方法について説明します"
}
</script>
{{% alert color="primary" %}}

Adobe Acrobat SDKは、Acrobat技術と連携するソフトウェアを開発するためのツールセットです。SDKには、ヘッダーファイル、型ライブラリ、シンプルなユーティリティ、サンプルコード、およびドキュメントが含まれています。

Acrobat SDKを使用すると、以下の方法でAcrobatおよびAdobe Readerと統合するソフトウェアを開発できます：

- **JavaScript** — AcrobatまたはAdobe Readerの機能を拡張するために、個別のPDFドキュメント内または外部でスクリプトを書きます。
- **プラグイン** — AcrobatまたはAdobe Readerの機能を拡張するために、動的にリンクされたプラグインを作成します。
- **アプリケーション間通信** — アプリケーション間通信（IAC）を使用してAcrobat機能を制御する別のアプリケーションプロセスを書きます。Microsoft® Windows®ではDDEおよびOLEがサポートされ、Mac OS®ではApple events/AppleScriptがサポートされます。UNIX®ではIACは利用できません。

Aspose.PDF for .NETは、Adobe Acrobat Automationに依存しないで済む、同様の機能を多く提供します。
Aspose.PDF for .NETはAdobe Acrobat Automationに依存しないで済む多くの同じ機能を提供します。

{{% /alert %}}

## Acrobat Interapplication通信APIを使用したアプリケーション開発

Acrobat APIを、Acrobat Interapplication Communication（IAC）オブジェクトを使用する2つの異なる層があると考えてください：

- Acrobatアプリケーション（AV）層。AV層では、ドキュメントの表示方法を制御できます。例えば、ドキュメントオブジェクトのビューはAcrobatに関連付けられた層に存在します。
- ポータブルドキュメント（PD）層。PD層は、ページなど、ドキュメント内の情報へのアクセスを提供します。PD層からは、ページの削除、移動、置換、アノテーション属性の変更など、PDFドキュメントの基本的な操作を実行できます。また、PDFページを印刷したり、テキストを選択したり、操作されたテキストにアクセスしたり、サムネイルを作成または削除したりすることもできます。

私たちの意図はPDFページをサムネイル画像に変換することなので、IACにより焦点を当てています。
PDFページをサムネイル画像に変換することを目的としているため、IACにより注力しています。

### Acrobat アプローチ

各ドキュメントのサムネイル画像を生成するために、Adobe Acrobat 7.0 SDKとMicrosoft .NET 2.0 Frameworkを使用しました。

[Acrobat SDK](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/)は、Adobe Acrobatの完全版と組み合わせることで、COMライブラリのオブジェクトを公開します（残念ながら無料のAdobe ReaderはCOMインターフェースを公開していません）。これらのCOMオブジェクトをCOM Interopを介して使用し、PDFドキュメントを読み込み、最初のページを取得し、そのページをクリップボードにレンダリングします。次に、.NET Frameworkを使用してこれをビットマップにコピーし、画像を拡大・結合して、結果をGIFまたはPNGファイルとして保存します。

Adobe Acrobatがインストールされたら、regedit.exeを使用してHKEY_CLASSES_ROOTの下を検索し、AcroExch.PDDocと呼ばれるエントリを探します。

**レジストリに表示されるAcroExch.PDDDocエントリ**

![todo:image_alt_text](generate-thumbnail-images-from-pdf-documents_1.png)
![todo:image_alt_text](generate-thumbnail-images-from-pdf-documents_1.png)

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-CreateThumbnailImagesUsingAdobe-CreateThumbnailImagesUsingAdobe.cs" >}}

## Aspose.PDF for .NETのアプローチ

Aspose.PDF for .NETはPDFドキュメントを扱うための広範なサポートを提供しています。また、PDFドキュメントのページをさまざまなイメージ形式に変換する機能もサポートしています。上記の機能はAspose.PDF for .NETを使用して簡単に実現できます。

Aspose.PDFの明確な利点:

- PDFファイルを扱うためにシステムにAdobe Acrobatをインストールする必要はありません。
- Acrobat Automationと比較して、Aspose.PDF for .NETの使用はシンプルで理解しやすいです。

PDFページをJPEGに変換する必要がある場合、[Aspose.PDF.Devices](https://reference.aspose.com/pdf/net/aspose.pdf.devices) 名前空間には、PDFページをJPEGイメージにレンダリングするための[JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice)というクラスが提供されています。

PDFページをJPEGに変換する必要がある場合、[Aspose.PDF.Devices](https://reference.aspose.com/pdf/net/aspose.pdf.devices) 名前空間は、PDFページをJPEG画像にレンダリングするための[JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice)というクラスを提供しています。

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-CreateThumbnailImages-CreateThumbnailImages.cs" >}}

{{% alert color="primary" %}}

- CodeProjectに感謝します：[PDFドキュメントからサムネイル画像を生成する](https://www.codeproject.com/Articles/5887/Generate-Thumbnail-Images-from-PDF-Documents)。
- Acrobatに感謝します：[Acrobat SDKリファレンス](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/documentation.html)。

{{% /alert %}}

