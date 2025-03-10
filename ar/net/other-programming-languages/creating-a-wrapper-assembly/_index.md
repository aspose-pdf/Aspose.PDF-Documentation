---
title: إنشاء تجميع غلاف
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ar/net/creating-a-wrapper-assembly/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Creating a Wrapper Assembly",
    "alternativeHeadline": "Simplify COM Interop with Wrapper Assemblies",
    "abstract": "تتيح ميزة تجميع الغلاف الجديدة لـ Aspose.PDF for .NET للمطورين إنشاء واجهة مبسطة للتفاعل مع فئات Aspose.PDF وطرقها وخصائصها من التعليمات البرمجية غير المدارة. من خلال احتواء تعقيد التفاعل مع COM، تعمل هذه الوظيفة على تبسيط تطوير المشروع، مما يجعل من الأسهل إدارة واستخدام وظائف PDF دون الحاجة إلى مهارات متقدمة في برمجة .NET",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "244",
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
    "url": "/net/creating-a-wrapper-assembly/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/creating-a-wrapper-assembly/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

{{% alert color="primary" %}}

إذا كنت بحاجة إلى استخدام العديد من فئات وطرق وخصائص Aspose.PDF for .NET، فكر في إنشاء تجميع غلاف (باستخدام C# أو أي لغة برمجة .NET أخرى). تساعد تجميعات الغلاف في تجنب استخدام Aspose.PDF for .NET مباشرة من التعليمات البرمجية غير المدارة.

نهج جيد هو تطوير تجميع .NET يشير إلى Aspose.PDF for .NET ويقوم بكل العمل معه، ويعرض فقط مجموعة محدودة من الفئات والطرق للتعليمات البرمجية غير المدارة. يجب أن تعمل تطبيقاتك بعد ذلك فقط مع مكتبة الغلاف الخاصة بك.

تقليل عدد الفئات والطرق التي تحتاج إلى استدعائها عبر التفاعل مع COM يبسط المشروع. غالبًا ما يتطلب استخدام فئات .NET عبر التفاعل مع COM مهارات متقدمة.

{{% /alert %}}

## تجميع غلاف Aspose.PDF for .NET

```csharp
using System.Runtime.InteropServices;

namespace TextRetriever
{
    [InterfaceType(ComInterfaceType.InterfaceIsIDispatch)]
    public interface IRetriever
    {
        [DispId(1)]
        void SetLicense(string file);

        [DispId(2)]
        string GetText(string file);
    }

    [ClassInterface(ClassInterfaceType.None)]
    [ComSourceInterfaces(typeof(IRetriever))]
    public class Retriever : IRetriever
    {
        public void SetLicense(string file)
        {
            var lic = new Aspose.Pdf.License();
            lic.SetLicense(file);
        }

        public string GetText(string file)
        {
            // Open PDF document
            using (var document = new Aspose.Pdf.Document(file))
            {
                // Create TextAbsorber object to extract text
                var absorber = new Aspose.Pdf.Text.TextAbsorber();

                // Accept the absorber for all document's pages
                document.Pages.Accept(absorber);

                // Get the extracted text
                string text = absorber.Text;

                return text;
            }
        }
    }
}
```