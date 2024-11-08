---
title: PDFでのAcroFormsの操作
linktitle: AcroForms
type: docs
weight: 10
url: /ja/php-java/acroforms/
description: Aspose.PDF for PHP via Javaを使用すると、フォームをゼロから作成したり、PDFドキュメント内のフォームフィールドに入力したり、フォームからデータを抽出したり、既存のフォームにフィールドを追加または削除したりできます。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## AcroFormsの基本

**AcroForms**は、元々のPDFフォーム技術です。AcroFormsはページ指向のフォームです。1998年に初めて導入されました。Forms Data FormatまたはFDF、およびXML Forms Data FormatまたはxFDFで入力を受け付けます。サードパーティのベンダーはAcroFormsをサポートしています。AdobeがAcroFormsを導入した際には、Adobe Acrobat Pro/Standardで作成され、特別な種類の静的または動的なXFAフォームではない「PDFフォーム」として言及しました。AcroFormsは移植性があり、すべてのプラットフォームで動作します。

AcroFormsを使用して、PDFフォームドキュメントに追加のページを追加することができます。
 テンプレートの概念のおかげで、AcroFormsを使用して複数のデータベースレコードでフォームを入力することができます。

PDF 1.7は、データとPDFフォームを統合するための2つの異なる方法をサポートしています。

*AcroForms（アクロバットフォームとしても知られる）* は、PDF 1.2形式の仕様で導入され、含まれています。

*Adobe XML Forms Architecture (XFA) フォーム* は、PDF 1.5形式の仕様でオプション機能として導入されました。XFA仕様はPDF仕様には含まれておらず、参照のみされています。

**Acroforms** と **XFA** フォームを理解するためには、まず基本を理解する必要があります。まず、どちらも使用できるPDFフォームです。Acroformsは1998年に作成された古いもので、クラシックPDFフォームとして今でも言及されています。XFAフォームはPDFとして保存できるウェブページで、2003年に登場しました。PDFがXFAフォームを受け入れ始めるまでには少し時間がかかりました。

AcroFormsにはXFAにはない機能があり、逆にXFAにはAcroFormsにない機能があります。例えば：

- AcroFormsは「テンプレート」の概念をサポートしており、複数のデータベースレコードでフォームを入力するために追加ページをPDFフォームドキュメントに追加することができます。- XFAは、データに合わせてフィールドをリサイズできるようにするドキュメントリフローの概念をサポートしています。

そのため、PDFは電子的に配布でき、文書内で情報を入力し、従来の郵便で印刷したり発送したりすることなく送信者に返送できるため、フォームに最適なファイル形式です。

フォームを扱う可能性についての詳細な研究をするには、次の記事をセクションで参照してください：

-[AcroFormを作成する](/pdf/ja/php-java/create-form/) - PHPを使用して、RadioButtonField、TextBoxField、Caption Fieldを追加し、ゼロからフォームを作成します。

-[AcroFormに入力する](/pdf/ja/php-java/fill-form/) - フォームフィールドに入力するには、ドキュメントオブジェクトのFormコレクションからフィールドを取得します。

-[AcroFormのデータを抽出する](/pdf/ja/php-java/extract-form/) - すべてのフィールドや個々のフィールドから値を取得するなど。

-[AcroFormを修正する](/pdf/ja/php-java/modifing-form/) - FieldLimitを取得/設定し、既存のフォームのフィールドを削除し、PHPで14のコアPDFフォント以外のフォームフィールドフォントを設定します。