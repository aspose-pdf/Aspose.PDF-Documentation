---
title: AcroFormを埋める - Pythonを使用してPDFフォームを埋める
linktitle: AcroFormを埋める
type: docs
weight: 20
url: ja/python-net/fill-form/
keywords: PythonでPDFフォームを埋める
description: Aspose.PDF for Pythonライブラリを使用して、PDFドキュメント内のフォームに記入できます。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "AcroFormを埋める",
    "alternativeHeadline": "PDFでAcroFormを埋める方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdfドキュメント生成",
    "keywords": "pdf, python, acroformを埋める",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/fill-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/fill-form/"
    },
    "dateModified": "2023-02-04",
    "description": "Aspose.PDF for Pythonライブラリを使用して、PDFドキュメント内のフォームに記入できます。"
}
</script>


## PDF ドキュメントのフォームフィールドに入力する

フォームフィールドに入力するには、Document オブジェクトの [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) コレクションからフィールドを取得します。次に、フィールドの [value](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/#properties) プロパティを使用してフィールド値を設定します。

この例では、[TextBoxField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/) を選択し、Value プロパティを使用してその値を設定します。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    pdfDocument = ap.Document(input_file)
    for formField in pdfDocument.form.fields:
        if formField.partial_name == "Field 1":
            # フィールド値を変更
            formField.value = "777"

    # 更新されたドキュメントを保存
    pdfDocument.save(output_pdf)