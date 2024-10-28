---
title: PDFでのテキスト注釈の使用
linktitle: テキスト注釈
type: docs
weight: 10
url: /net/text-annotation/
description: Aspose.PDF for .NETでは、PDFドキュメントからテキスト注釈を追加、取得、削除することができます。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFでのテキスト注釈の使用",
    "alternativeHeadline": "PDFにテキスト注釈を追加する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, テキスト注釈",
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
    "url": "/net/text-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NETでは、PDFドキュメントからテキスト注釈を追加、取得、削除することができます。"
}
</script>
## 既存のPDFファイルにテキスト注釈を追加する方法

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリでも動作します。

テキスト注釈は、PDFドキュメントの特定の場所に添付される注釈です。閉じているときはアイコンとして表示され、開いているときは、読者が選択したフォントとサイズでメモテキストを含むポップアップウィンドウが表示されるべきです。

注釈は、特定のページの [Annotations](https://reference.aspose.com/pdf/net/aspose.pdf.annotations) コレクションに含まれています。このコレクションはその個々のページの注釈のみを含み、各ページには独自のAnnotationsコレクションがあります。

特定のページに注釈を追加するには、そのページのAnnotationsコレクションに[Add](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection/methods/add) メソッドを使用して追加します。

1. 最初に、PDFに追加したい注釈を作成します。
1. 次に、入力PDFを開きます。
1.

次のコードスニペットは、PDFページに注釈を追加する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "AddAnnotation.pdf");

// 注釈を作成する
TextAnnotation textAnnotation = new TextAnnotation(pdfDocument.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600));
textAnnotation.Title = "サンプルの注釈タイトル";
textAnnotation.Subject = "サンプルのサブジェクト";
textAnnotation.State = AnnotationState.Accepted;
textAnnotation.Contents = "注釈のサンプルコンテンツ";
textAnnotation.Open = true;
textAnnotation.Icon = TextIcon.Key;

Border border = new Border(textAnnotation);
border.Width = 5;
border.Dash = new Dash(1, 1);
textAnnotation.Border = border;
textAnnotation.Rect = new Aspose.Pdf.Rectangle(200, 400, 400, 600);

// ページの注釈コレクションに注釈を追加する
pdfDocument.Pages[1].Annotations.Add(textAnnotation);
dataDir = dataDir + "AddAnnotation_out.pdf";
// 出力ファイルを保存する
pdfDocument.Save(dataDir);
```
## ポップアップ注釈の追加方法

ポップアップ注釈は、入力および編集のためにポップアップウィンドウにテキストを表示します。それは単独では表示されず、親の注釈、マークアップ注釈と関連付けられており、親のテキストの編集に使用されます。

自身の表示ストリームや関連アクションを持たず、親の注釈辞書のPopupエントリによって識別されます。

次のコードスニペットは、[ポップアップ注釈](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/popupannotation) をPDFページに追加する方法を示しています。親の[ライン注釈](/pdf/net/figures-annotation/#how-to-add-line-annotation-into-existing-pdf-file)の追加例を使用しています。

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.Linq;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleLineAnnotation
    {
        // ドキュメントディレクトリへのパス
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddLineAnnotation()
        {
            try
            {
                // PDFファイルをロード
                Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments.pdf"));

                // ライン注釈を作成
                var lineAnnotation = new LineAnnotation(
                    document.Pages[1],
                    new Rectangle(550, 93, 562, 439),
                    new Point(556, 99), new Point(556, 443))
                {
                    Title = "John Smith",
                    Color = Color.Red,
                    Width = 3,
                    StartingStyle = LineEnding.OpenArrow,
                    EndingStyle = LineEnding.OpenArrow,
                    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 124, 1021, 266))
                };

                // 注釈をページに追加
                document.Pages[1].Annotations.Add(lineAnnotation);
                document.Save(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
```
## 新しいフリーテキスト注釈を追加（または作成）する方法

フリーテキスト注釈は、ページに直接テキストを表示します。[PdfContentEditor.CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) メソッドは、このタイプの注釈を作成することを可能にします。次のスニペットでは、文字列の最初の出現の上にフリーテキスト注釈を追加します。

```csharp
private static void AddFreeTextAnnotationDemo()
{
    _document = new Document(@"C:\tmp\pdf-sample.pdf");
    var pdfContentEditor = new PdfContentEditor(_document);

    tfa.Visit(_document.Pages[1]);
    if (tfa.TextFragments.Count <= 0) return;
    var rect = new System.Drawing.Rectangle
    {
        X = (int)tfa.TextFragments[1].Rectangle.LLX,
        Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
        Height = 18,
        Width = 100
    };

    pdfContentEditor.CreateFreeText(rect, "Free Text Demo", 1); // last param is a page number
    pdfContentEditor.Save(@"C:\tmp\pdf-sample-0.pdf");
}
```

### フリーテキスト注釈のコールアウトプロパティを設定する
### FreeTextAnnotationのCalloutプロパティを設定する

PDFドキュメントの注釈設定をより柔軟に行うために、Aspose.PDF for .NETは[FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation)クラスの[Callout](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation/properties/callout)プロパティを提供しています。これにより、コールアウトラインのポイントの配列を指定できます。次のコードスニペットは、この機能を使用する方法を示しています：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Document doc = new Document();
Page page = doc.Pages.Add();
DefaultAppearance da = new DefaultAppearance();
da.TextColor = System.Drawing.Color.Red;
da.FontSize = 10;
FreeTextAnnotation fta = new FreeTextAnnotation(page, new Rectangle(422.25, 645.75, 583.5, 702.75), da);
fta.Intent = FreeTextIntent.FreeTextCallout;
fta.EndingStyle = LineEnding.OpenArrow;
fta.Callout = new Point[]
{
    new Point(428.25,651.75), new Point(462.75,681.375), new Point(474,681.375)
};
page.Annotations.Add(fta);
fta.RichText = "<body xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:xfa=\"http://xfa.org/schema/xfa-data/1.0/\" xfa:APIVersion=\"Acrobat:11.0.23\" xfa:spec=\"2.0.2\"  style=\"color:#FF0000;font-weight:normal;font-style:normal;font-stretch:normal\"><p dir=\"ltr\"><span style=\"font-size:9.0pt;font-family:Helvetica\">これはサンプルです</span></p></body>";
doc.Save(dataDir + "SetCalloutProperty.pdf");
```
### XFDFファイルのコールアウトプロパティを設定

XFDFファイルからインポートを使用する場合は、単にCalloutではなくcallout-line名を使用してください。次のコードスニペットは、この機能を使用する方法を示しています：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
Document pdfDocument = new Document(dataDir + "AddAnnotation.pdf");
StringBuilder Xfdf = new StringBuilder();
Xfdf.AppendLine("<?xml version=\"1.0\" encoding=\"UTF-8\"?><xfdf xmlns=\"http://ns.adobe.com/xfdf/\" xml:space=\"preserve\"><annots>");
CreateXfdf(ref Xfdf);
Xfdf.AppendLine("</annots></xfdf>");
pdfDocument.ImportAnnotationsFromXfdf(new MemoryStream(Encoding.UTF8.GetBytes(Xfdf.ToString())));
pdfDocument.Save(dataDir + "SetCalloutPropertyXFDF.pdf");
```

次のメソッドがXFDFの作成に使用されています：

```csharp
/// <summary>
/// XFDFを作成する
/// </summary>
/// <param name="pXfdf"></param>

static void CreateXfdf(ref StringBuilder pXfdf)
{
    pXfdf.Append("<freetext");
    pXfdf.Append(" page=\"0\"");
    pXfdf.Append(" rect=\"422.25,645.75,583.5,702.75\"");
    pXfdf.Append(" intent=\"FreeTextCallout\"");
    pXfdf.Append(" callout-line=\"428.25,651.75,462.75,681.375,474,681.375\"");
    pXfdf.Append(" tail=\"OpenArrow\"");
    pXfdf.AppendLine(">");
    pXfdf.Append("<contents-richtext><body ");
    pXfdf.Append(" style=\"font-size:10.0pt;text-align:left;color:#FF0000;font-weight:normal;font-style:normal;font-family:Helvetica;font-stretch:normal\">");
    pXfdf.Append("<p dir=\"ltr\">This is a sample</p>");
    pXfdf.Append("</body></contents-richtext>");
    pXfdf.AppendLine("<defaultappearance>/Helv 12 Tf 1 0 0 rg</defaultappearance>");
    pXfdf.AppendLine("</freetext>");
}
```
### フリーテキスト注釈を非表示にする

文書を見る際には見えないが、印刷時には見えるような透かしを作成する必要がある場合があります。この目的のために注釈フラグを使用します。以下のコードスニペットで方法を示します。

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// ドキュメントを開く
Document doc = new Document(dataDir + "input.pdf");

FreeTextAnnotation annotation = new FreeTextAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(50, 600, 250, 650), new DefaultAppearance("Helvetica", 16, System.Drawing.Color.Red));
annotation.Contents = "ABCDEFG";
annotation.Characteristics.Border = System.Drawing.Color.Red;
annotation.Flags = AnnotationFlags.Print | AnnotationFlags.NoView;
doc.Pages[1].Annotations.Add(annotation);

dataDir = dataDir + "InvisibleAnnotation_out.pdf";
// 出力ファイルを保存
doc.Save(dataDir);
```
### FreeTextAnnotationのフォーマット設定

この部分では、フリーテキスト注釈のテキストをフォーマットする方法について説明します。

注釈は、[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)オブジェクトの[AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection)コレクションに含まれています。PDF文書に[FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation)を追加する際には、[DefaultAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/defaultappearance/methods/index)クラスを使用して、フォント、サイズ、色などのフォーマット情報を指定することができます。また、TextStyleプロパティを使用してフォーマット情報を指定することも可能です。さらに、PDF文書内の任意のFreeTextAnnotationのフォーマットを更新することができます。

[TextStyle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textstyle)クラスは、デフォルトスタイルエントリの操作をサポートしています。
[TextStyle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textstyle) クラスは、デフォルトスタイルエントリの操作をサポートしています。

- FontName プロパティは、フォント名を取得または設定します（文字列）。
- FontSize プロパティは、デフォルトのテキストサイズを取得および設定します（double）。
- System.Drawing.Color プロパティは、テキストの色を取得および設定します（色）。
- TextAlignment プロパティは、注釈のテキストアライメントを取得および設定します（アライメント）。

次のコードスニペットは、特定のテキストフォーマットで FreeTextAnnotation を追加する方法を示しています。

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Annotations-SetFreeTextAnnotationFormatting-SetFreeTextAnnotationFormatting.cs" >}}

{{% alert color="primary" %}}

フリーテキスト注釈の内容またはテキストスタイルを変更すると、注釈の外観が変更を反映するように再生成されます。

{{% /alert %}}

### StrikeOutAnnotation を使用して単語を打ち消す

Aspose.PDF for .NET では、PDFドキュメントの注釈を追加、削除、更新することができます。
Aspose.PDF for .NETは、PDFドキュメント内のアノテーションを追加、削除、更新することができます。

特定のTextFragmentに取り消し線を引くためには：

1. PDFファイル内でTextFragmentを検索します。
1. TextFragmentオブジェクトの座標を取得します。
1. 座標を使用してStrikeOutAnnotationオブジェクトをインスタンス化します。

次のコードスニペットは、特定のTextFragmentを検索し、そのオブジェクトにStrikeOutAnnotationを追加する方法を示しています。

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Annotations-StrikeOutWords-StrikeOutWords.cs" >}}

{{% alert color="primary" %}}

この機能はバージョン19.6以降でサポートされています。

{{% /alert %}}

## PDFファイルのページからすべてのアノテーションを削除

[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)オブジェクトの[AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection)コレクションには、その特定のページのすべてのアノテーションが含まれています。
[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)オブジェクトの[AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection)コレクションには、その特定のページのすべての注釈が含まれています。

次のコードスニペットは、特定のページからすべての注釈を削除する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "DeleteAllAnnotationsFromPage.pdf");

// 特定の注釈を削除
pdfDocument.Pages[1].Annotations.Delete();

dataDir = dataDir + "DeleteAllAnnotationsFromPage_out.pdf";
// 更新されたドキュメントを保存
pdfDocument.Save(dataDir);
```

## PDFファイルから特定の注釈を削除

{{% alert color="primary" %}}

このリンクでAspose.PDFの品質を確認し、結果をオンラインで取得できます：
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)

{{% /alert %}}

Aspose.PDFを使用すると、PDFファイルから特定の注釈を削除できます。このトピックでは、その方法について説明します。

PDFから特定の注釈を削除するには、[ページ](https://reference.aspose.com/pdf/net/aspose.pdf/page)オブジェクトに属する[AnnotationCollectionコレクションのDeleteメソッド](https://reference.aspose.com/pdf/net/aspose.pdf.annotations.annotationcollection/delete/methods/1)を呼び出します。Deleteメソッドは、削除する注釈のインデックスを必要とします。その後、更新されたPDFファイルを保存します。次のコードスニペットは、特定の注釈を削除する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "DeleteParticularAnnotation.pdf");

// 特定の注釈を削除
pdfDocument.Pages[1].Annotations.Delete(1);

dataDir = dataDir + "DeleteParticularAnnotation_out.pdf";
// 更新されたドキュメントを保存
pdfDocument.Save(dataDir);
```
## PDFドキュメントのページからすべての注釈を取得する

Aspose.PDFを使用すると、ドキュメント全体または指定されたページから注釈を取得できます。PDFドキュメントのページからすべての注釈を取得するには、目的のページリソースの[AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection)コレクションをループします。次のコードスニペットは、ページのすべての注釈を取得する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "GetAllAnnotationsFromPage.pdf");

// すべての注釈をループする
foreach (MarkupAnnotation annotation in pdfDocument.Pages[1].Annotations)
{
    // 注釈のプロパティを取得する
    Console.WriteLine("タイトル : {0} ", annotation.Title);
    Console.WriteLine("件名 : {0} ", annotation.Subject);
    Console.WriteLine("内容 : {0} ", annotation.Contents);
}
```
PDF全体からすべての注釈を取得するには、AnnotationCollectionクラスコレクションをナビゲートする前に、ドキュメントのPageCollectionクラスコレクションをループする必要があります。コレクションの各注釈をMarkupAnnotationクラスという基本注釈タイプで取得し、そのプロパティを表示できます。

## PDFファイルから特定の注釈を取得する

注釈は個々のページに関連付けられており、[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)オブジェクトの[AnnotationCOllection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection)コレクションに格納されています。
アノテーションは個々のページに関連付けられ、[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) オブジェクトの [AnnotationCOllection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) コレクションに保存されます。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "GetParticularAnnotation.pdf");

// 特定のアノテーションを取得
TextAnnotation textAnnotation = (TextAnnotation)pdfDocument.Pages[1].Annotations[1];

// アノテーションのプロパティを取得
Console.WriteLine("Title : {0} ", textAnnotation.Title);
Console.WriteLine("Subject : {0} ", textAnnotation.Subject);
Console.WriteLine("Contents : {0} ", textAnnotation.Contents);
```

## アノテーションのリソースを取得する

Aspose.PDF は、ドキュメント全体または特定のページからアノテーションのリソースを取得することができます。
Aspose.PDFを使用すると、ドキュメント全体または指定されたページから注釈のリソースを取得できます。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// ドキュメントを開く
Document doc = new Document(dataDir + "AddAnnotation.pdf");
// 注釈を作成
ScreenAnnotation sa = new ScreenAnnotation(doc.Pages[1], new Rectangle(100, 400, 300, 600), dataDir + "AddSwfFileAsAnnotation.swf");
doc.Pages[1].Annotations.Add(sa);
// ドキュメントを保存
doc.Save(dataDir + "GetResourceOfAnnotation_Out.pdf");

// ドキュメントを開く
Document doc1 = new Document(dataDir + "GetResourceOfAnnotation_Out.pdf");

// 注釈のアクションを取得
RenditionAction action = (doc.Pages[1].Annotations[1] as ScreenAnnotation).Action as RenditionAction;

// レンディションアクションのレンディションを取得
Rendition rendition = ((doc.Pages[1].Annotations[1] as ScreenAnnotation).Action as RenditionAction).Rendition;

// メディアクリップ
MediaClip clip = (rendition as MediaRendition).MediaClip;
FileSpecification data = (clip as MediaClipData).Data;
MemoryStream ms = new MemoryStream();
byte[] buffer = new byte[1024];
int read = 0;
// メディアのデータはFileSpecification.Contentsでアクセス可能
Stream source = data.Contents;
while ((read = source.Read(buffer, 0, buffer.Length)) > 0)
{
    ms.Write(buffer, 0, read);
}
Console.WriteLine(rendition.Name);
Console.WriteLine(action.RenditionOperation);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
                "contactType": "販売",
                "areaServed": "US",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "販売",
                "areaServed": "GB",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "販売",
                "areaServed": "AU",
                "availableLanguage": "英語"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": ".NET用PDF操作ライブラリ",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

