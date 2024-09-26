---
title: קבלה והגדרה של מאפייני דף
type: docs
url: /net/get-and-set-page-properties/
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "קבלה והגדרה של מאפייני דף",
    "alternativeHeadline": "קבלה והגדרה של מאפייני דף PDF",
    "author": {
        "@type": "Person",
        "name":"אנסטסיה הולוב",
        "givenName": "אנסטסיה",
        "familyName": "הולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, קבלת מאפייני דף, הגדרת מאפייני דף",
    "wordcount": "302",
    "proficiencyLevel":"מתחיל",
    "publisher": {
        "@type": "Organization",
        "name": "צוות Aspose.PDF Doc",
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
                "contactType": "מכירות",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "מכירות",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "מכירות",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-and-set-page-properties/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
Aspose.PDF עבור .NET מאפשר לך לקרוא ולהגדיר מאפיינים של דפים בקובץ PDF ביישומי .NET שלך. סעיף זה מציג איך לקבל את מספר הדפים בקובץ PDF, לקבל מידע על מאפייני דף PDF כמו צבע ולהגדיר מאפייני דף. הדוגמאות שניתנות הן ב-C# אך ניתן להשתמש בכל שפת .NET כמו VB.NET כדי להשיג את אותו הדבר.

הקטע הבא גם עובד עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## קבלת מספר הדפים בקובץ PDF

כשעובדים עם מסמכים, לעיתים רוצים לדעת כמה דפים הם מכילים. עם Aspose.PDF זה לוקח לא יותר משתי שורות קוד.

כדי לקבל את מספר הדפים בקובץ PDF:

1. פתח את הקובץ PDF באמצעות המחלקה [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. לאחר מכן השתמש במאפיין Count של אוסף [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) (מאובייקט ה-Document) כדי לקבל את מספר הדפים הכולל במסמך.

הקטע הבא מראה איך לקבל את מספר הדפים של קובץ PDF.
הקטע הבא מראה איך לקבל את מספר העמודים בקובץ PDF.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetNumberofPages-GetNumberofPages.cs" >}}

### קבלת מונה עמודים ללא שמירת המסמך

לעיתים אנו מייצרים קבצי PDF על המעוף ובמהלך יצירת קובץ PDF, ייתכן שנתקל בדרישה (יצירת תוכן עניינים וכדומה) לקבל את מונה העמודים של קובץ PDF ללא שמירת הקובץ על המערכת או על זרם. כדי לענות על דרישה זו, הוצגה שיטה [ProcessParagraphs](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/processparagraphs) במחלקת המסמכים. אנא עיין בקטע הקוד הבא שמראה את השלבים לקבלת מונה העמודים ללא שמירת המסמך.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetPageCount-GetPageCount.cs" >}}

## קבלת מאפייני עמוד

לכל עמוד בקובץ PDF יש מספר מאפיינים, כגון רוחב, גובה, bleed-, crop- ו-trimbox.
### **הבנת תכונות דף: ההבדל בין ארטבוקס, בלידבוקס, קרופבוקס, מדיהבוקס, טרימבוקס לבין תכונת הרקט**

- **מדיה בוקס**: מדיה בוקס הוא תיבת הדף הגדולה ביותר. היא מתאימה לגודל הדף (לדוגמה A4, A5, מכתב אמריקאי וכו') שנבחר בעת הדפסת המסמך לפוסטסקריפט או PDF. במילים אחרות, מדיה בוקס קובע את הגודל הפיזי של המדיה שעליה מוצג או מודפס המסמך.
- **בליד בוקס**: אם למסמך יש בליד, גם ל-PDF יהיה בליד בוקס. בליד הוא כמות הצבע (או האמנות) המתרחבת מעבר לשולי הדף. הוא משמש לוודא שכאשר המסמך מודפס וחתוך לגודל ("מגוזם"), הדיו יגיע עד לשולי הדף. אפילו אם הדף נחתך באופן לא מדויק - חתך מעט מחוץ לסימני החיתוך - לא יופיעו שוליים לבנים על הדף.
- **טרים בוקס**: טרים בוקס מציין את הגודל הסופי של מסמך לאחר הדפסה וגיזום.
- **Trim box**: תיבת החיתוך מציינת את הגודל הסופי של מסמך לאחר הדפסה וחיתוך.
- **Art box**: תיבת האמנות היא התיבה שמצוירת סביב התוכן האמיתי של הדפים במסמכים שלך. תיבת זו משמשת בעת ייבוא מסמכי PDF ביישומים אחרים.
- **Crop box**: תיבת החיתוך היא "גודל הדף" בו מוצג המסמך PDF שלך ב-Adobe Acrobat. בתצוגה רגילה, רק תוכן תיבת החיתוך מוצג ב-Adobe Acrobat.
  לתיאורים מפורטים של תכונות אלו, קרא את מפרט Adobe.Pdf, במיוחד 10.10.1 גבולות דף.
- **Page.Rect**: החיתוך (המלבן הנראה בדרך כלל) של MediaBox ו-DropBox. התמונה למטה ממחישה את התכונות הללו.

לפרטים נוספים, בקר ב[דף זה](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### **גישה לתכונות דף**

המחלקה [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) מספקת את כל התכונות הקשורות לדף PDF מסוים.
המחלקה [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) מספקת את כל התכונות הקשורות לדף PDF מסוים.

משם, ניתן לגשת לאובייקטים של דף בודד בעזרת האינדקס שלהם, או לעבור על האוסף בלולאת foreach, כדי לקבל את כל הדפים. כאשר מתבצעת גישה לדף בודד, ניתן לקבל את תכונותיו. קטע הקוד הבא מראה איך לקבל את תכונות הדף.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetProperties-GetProperties.cs" >}}

## לקבל דף מסוים של קובץ PDF

Aspose.PDF מאפשר לך [לפצל קובץ PDF לדפים בודדים](/pdf/net/split-pdf-document/) ולשמור אותם כקבצי PDF. לקבל דף מצוין בקובץ PDF ולשמור אותו כ-PDF חדש הוא פעולה דומה מאוד: פתח את המסמך המקורי, גש לדף, צור מסמך חדש והוסף את הדף אליו.

האובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) עם המחלקה [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) מחזיק את הדפים בקובץ PDF.
האובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) וה-[PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) שלו מכילים את הדפים בקובץ PDF.

1. ציין את מפתח הדף באמצעות התכונה Pages.
1. צור אובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) חדש.
1. הוסף את האובייקט [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) לאובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) החדש.
1. שמור את הפלט באמצעות השיטה [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

הקטע קוד הבא מראה איך לקבל דף מסוים מקובץ PDF ולשמור אותו כקובץ חדש.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetParticularPage-GetParticularPage.cs" >}}

## קביעת צבע הדף

הכיתה [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) מספקת את התכונות הקשורות לדף מסוים במסמך PDF, כולל איזה סוג של צבע - RGB, שחור לבן, גרייסקייל או לא מוגדר - הדף משתמש.
המחלקה [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) מספקת את התכונות הקשורות לדף מסוים במסמך PDF, כולל איזה סוג של צבע - RGB, שחור לבן, גרייסקייל או לא מוגדר - הדף משתמש.

כל דפי הקבצים PDF מכילים את אוסף ה-[PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection). תכונת ColorType מציינת את צבע האלמנטים בדף. כדי לקבל או לקבוע את מידע הצבע עבור דף PDF מסוים, השתמש בתכונת [ColorType](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/colortype) של אובייקט [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).

הקטע קוד הבא מראה כיצד לעבור בין עמודים בקובץ PDF כדי לקבל מידע על הצבע.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-DeterminePageColor-DeterminePageColor.cs" >}}

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

