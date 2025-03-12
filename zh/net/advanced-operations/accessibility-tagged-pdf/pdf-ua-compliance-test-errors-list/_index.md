---
title: PDF-UA 合规性测试 - 错误列表
linktitle: PDF-UA 合规性测试 - 错误列表
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /zh/net/pdf-ua-compliance-test-errors-list/
description: 本文展示了在使用 Aspose.PDF API 和 C# 或 VB 进行 PDF/UA 合规性测试时可能出现的错误列表。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF-UA Compliance Test - Errors List",
    "alternativeHeadline": "Comprehensive Error List for PDF-UA Compliance Testing",
    "abstract": "发现新的 PDF-UA 合规性测试功能，该功能简化了在使用 Aspose.PDF API 进行 PDF/UA 合规性测试时的错误识别。此功能提供了按类型分类的错误消息的综合列表，使开发人员能够高效地排除故障并确保其 PDF 文档的可访问性合规性。通过对常见合规性错误的清晰洞察，增强您的开发过程，从一般问题到特定图形和文本验证。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF-UA compliance, Aspose.PDF API, compliance testing errors, document generation, C# PDF handling, PDF/UA errors list, PDF validation messages, accessibility compliance, PDF error codes, structured document compliance",
    "wordcount": "1372",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "url": "/net/pdf-ua-compliance-test-errors-list/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-ua-compliance-test-errors-list/"
    },
    "dateModified": "2024-11-25",
    "description": "本文展示了在使用 Aspose.PDF API 和 C# 或 VB 进行 PDF/UA 合规性测试时可能出现的错误列表。"
}
</script>

在使用 Aspose.PDF API 进行 PDF/UA 合规性测试时，您可能会对可以获得的错误消息感兴趣。这些错误有不同的类型，例如一般、文本、字体、标题等。有关这些错误的信息可以帮助您了解错误的确切原因及其处理方式。

在本文中，我们列出了在使用 API 进行 PDF/UA 合规性测试时可能出现的错误。

## **一般**

|**代码**|**严重性**|**消息**|
| :- | :- | :- |
|5:1|错误|缺少 PDF/UA 标识符|
|6.2:1.1|错误|结构父树：发现不一致条目|
|7.1:1.1(14.8.1)|错误|文档未标记为标记|
|7.1:1.1(14.8)|错误|未标记的 [OBJECT_NAME] 对象|
|7.1:1.2(14.8.2.2)|错误|标记内容内存在伪影|
|7.1:1.3(14.8.2.2)|错误|伪影内存在标记内容|
|7.1:2.1|警告|缺少结构树|
|7.1:2.2|警告|发现的“文档”结构元素不是根元素|
|7.1:2.3|警告|‘[ELEMENT_NAME]’ 结构元素用作根元素|
|7.1:2.4.1|警告|可能不当使用‘[ELEMENT_NAME]’ 结构元素|
|7.1:2.4.2|错误|‘[ELEMENT_NAME]’ 结构元素使用无效|
|7.1:2.5|警告|可能错误地将‘[ELEMENT_NAME]’ 结构元素嵌套到 StructTreeRoot 中|
|7.1:3(14.8.4)|错误|非标准结构类型‘[TYPE_NAME]’既未映射到标准结构类型，也未映射到其他非标准结构类型|
|7.1:4(14.8.4)|警告|标准结构类型‘[TYPE_NAME]’被重新映射为‘[TYPE_NAME]’|
|7.1:5|需要手动检查|颜色对比|
|7.1:6.1|错误|文档中缺少 XMP 元数据|
|7.1:6.2|错误|文档的 XMP 元数据中缺少标题|
|7.1:6.3|警告|文档的 XMP 元数据中的标题为空|
|7.1:7.1(12.2)|警告|缺少‘ViewerPreferences’字典|
|7.1:7.2(12.2)|错误|‘DisplayDocTitle’ 条目未设置|
|7.1:8(14.7.1)|错误|‘Suspects’ 条目已设置|
|7.1:9.1(14.7)|错误|页面中缺少‘StructParents’ 键|
|7.1:9.2(14.7)|错误|注释中缺少‘StructParent’ 条目|
|7.1:9.3(14.7)|错误|未找到给定‘StructParents’的条目|

## **文本**

|**代码**|**严重性**|**消息**|
| :- | :- | :- |
|7.2:1|需要手动检查|逻辑阅读顺序|
|7.2:2(14.8.2.4.2)|错误|文本对象中的字符无法映射到 Unicode|
|7.2:3.1(14.9.2.2)|错误|无法确定文本对象的自然语言|
|7.2:3.2(14.9.2.2)|错误|无法确定替代文本的自然语言|
|7.2:3.3(14.9.2.2)|错误|无法确定实际文本的自然语言|
|7.2:3.4(14.9.2.2)|错误|无法确定扩展文本的自然语言|
|7.2:4(14.9.4)|错误|可伸缩字符未使用 ActualText 标记|

## **字体**

|**条款**|**严重性**|**消息**|
| :- | :- | :- |
|7.21.3.1|错误|CIDFont 中的字符集合与内部 CMap 的字符集合不兼容|
|7.21.3.2|错误|字体‘[FONT_NAME]’中的 CIDToGIDMap 未嵌入或不完整|
|7.21.3.2|错误|字体‘[FONT_NAME]’未嵌入 CMap|
|7.21.4.2|错误|字体‘[FONT_NAME]’缺少或不完整的 CIDSet|
|7.21.4.2|错误|嵌入字体‘[FONT_NAME]’中缺少字形|
|7.21.6|错误|非符号 TrueType 字体‘[FONT_NAME]’没有 cmap 条目|
|7.21.6|错误|符号 TrueType 字体‘[FONT_NAME]’禁止编码条目|
|7.21.6|错误|TrueType 字体‘[FONT_NAME]’使用了不正确的编码|
|7.21.6|错误|非符号 TrueType 字体‘[FONT_NAME]’的“Differences”数组不正确|

## **图形**

|**代码**|**严重性**|**消息**|
| :- | :- | :- |
|7.3:1(14.8.4.5)|错误|单页上的‘[ELEMENT_NAME]’元素没有边界框|
|7.3:2|错误|缺少‘[ELEMENT_NAME]’结构元素的替代文本|
|7.3:3|错误|缺少伴随图形的标题|
|7.3:4(14.8.4.5)|错误|图形对象出现在 BT 和 ET 操作符之间|

## **标题**

|**代码**|**严重性**|**消息**|
| :- | :- | :- |
|7.4.2:1|错误|第一个标题不是第一级|
|7.4.2:2|错误|编号标题跳过一个或多个标题级别|
|7.4.4:1|错误|发现‘H’和‘Hn’结构元素|
|7.4.4:2|错误|父结构元素内存在多个‘H’结构元素|

## **表格**

|**代码**|**严重性**|**消息**|
| :- | :- | :- |
|7.5:1|警告|不规则表格行|
|7.5:2|错误|表头单元格没有关联的子单元格|
|7.5:3.1|警告|缺少表头|
|7.5:3.2|警告|缺少表格摘要|

## **列表**

|**代码**|**严重性**|**消息**|
| :- | :- | :- |
|7.6:1|错误|‘LI’结构元素必须是‘L’元素的子元素|
|7.6:2|错误|‘Lbl’和‘LBody’结构元素必须是‘LI’元素的子元素|

## **注释和参考**

|**代码**|**严重性**|**消息**|
| :- | :- | :- |
|7.9:2.1|错误|‘Note’结构元素中缺少 ID|
|7.9:2.2|错误|‘Note’结构元素中的 ID 条目不是唯一的|

## **可选内容**

|**代码**|**严重性**|**消息**|
| :- | :- | :- |
|7.10:1|错误|可选内容配置字典中缺少‘Name’|
|7.10:2|错误|可选内容配置字典包含‘AS’键|

## **嵌入文件**

|**代码**|**严重性**|**消息**|
| :- | :- | :- |
|7.11:1|错误|文件规范中缺少‘F’或‘UF’键|
|7.11:2|警告|文件规范中缺少‘Desc’键|

## **数字签名**

|**代码**|**严重性**|**消息**|
| :- | :- | :- |
|7.13:1|错误|签名表单字段‘[FIELD_NAME]’不符合规范|
|7.13:2.1|错误|无法确定表单字段‘[FIELD_NAME]’的替代名称的自然语言|
|7.13:2.2|错误|表单字段‘[FIELD_NAME]’中缺少替代字段名称条目|

## **非交互式表单**

|**代码**|**严重性**|**消息**|
| :- | :- | :- |
|7.14:1|错误|非交互式表单项中缺少‘PrintField’属性|

## **XFA**

|**代码**|**严重性**|**消息**|
| :- | :- | :- |
|7.15:1|错误|PDF 包含动态 XFA 表单|

## **安全性**

|**代码**|**严重性**|**消息**|
| :- | :- | :- |
|7.16:1(7.6.3.2)|错误|安全设置阻止辅助技术访问文档内容|
|7.16:2(7.6.3.2)|错误|由于权限限制，不允许转换|

## **导航**

|**代码**|**严重性**|**消息**|
| :- | :- | :- |
|7.17:1|错误|文档大纲错误|
|7.17:2|错误|可以确定大纲的自然语言|
|7.17:3|需要手动检查|语义上适当的页面标签|

## **注释**

|**代码**|**严重性**|**消息**|
| :- | :- | :- |
|7.18.1:1|错误|无法确定目录条目的自然语言|
|7.18.1:2|错误|注释缺少替代描述|
|7.18.1:3|错误|注释未嵌套在‘Annot’结构元素内|
|7.18.2:1|错误|在 ISO 32000 中未定义子类型的注释不符合 7.18.1|
|7.18.2:2|错误|存在子类型为 TrapNet 的注释|
|7.18.3:1|错误|带有注释的页面中的标签顺序条目未设置为 'S'（结构）|
|7.18.4:1|错误|‘Widget’注释未嵌套在‘Form’结构元素内|
|7.18.5:1|错误|‘Link’注释未嵌套在‘Link’结构元素内|
|7.18.6.2:1|错误|媒体剪辑数据字典中缺少 CT 键|
|7.18.6.2:2|错误|媒体剪辑数据字典中缺少 Alt 键|
|7.18.7:1|错误|文件附件注释。文件规范中缺少‘F’或‘UF’键|
|7.18.7:2|警告|文件附件注释。文件规范中缺少‘Desc’键|
|7.18.8:1|错误|逻辑结构中包含打印标记注释|
|7.18.8:2|错误|打印标记注释的外观流未标记为伪影|

## **操作**

|**代码**|**严重性**|**消息**|
| :- | :- | :- |
|7.19:1|需要手动检查|发现操作。需要根据规范 PDF/UA 手动检查操作|

## **XObjects**

|**代码**|**严重性**|**消息**|
| :- | :- | :- |
|7.20:1|错误|在符合 PDF/UA 文件中不得使用引用 XObject|
|7.20:2|错误|表单 XObject 的内容未纳入结构元素|

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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
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