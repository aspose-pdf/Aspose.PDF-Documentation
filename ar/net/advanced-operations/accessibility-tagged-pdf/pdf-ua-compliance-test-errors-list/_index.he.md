---
title: רשימת שגיאות במבחן התאימות של PDF-UA
linktitle: רשימת שגיאות במבחן התאימות של PDF-UA
type: docs
weight: 50
url: /ar/net/pdf-ua-compliance-test-errors-list/
description: מאמר זה מציג רשימה של השגיאות שעלולות להתרחש במהלך בדיקת התאימות ל-PDF/UA באמצעות ממשק ה-API של Aspose.PDF ו-C# או VB.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "רשימת שגיאות במבחן התאימות של PDF-UA",
    "alternativeHeadline": "בדיקת התאימות ל-PDF/UA באמצעות ה-API",
    "author": {
        "name":"אנסטסיה חולוב",
        "givenName": "אנסטסיה",
        "familyName": "חולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכים PDF",
    "keywords": "pdf, c#, יצירת מסמכים",
    "wordcount": "302",
    "proficiencyLevel":"מתחיל",
    "publisher": {
        "@type": "Organization",
        "name": "צוות מסמכי Aspose.PDF",
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
    "url": "/net/pdf-ua-compliance-test-errors-list/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-ua-compliance-test-errors-list/"
    },
    "dateModified": "2022-02-04",
    "description": "מאמר זה מציג רשימה של השגיאות שעלולות להתרחש במהלך בדיקת התאימות ל-PDF/UA באמצעות ממשק ה-API של Aspose.PDF ו-C# או VB."
}
</script>
בעת ביצוע בדיקת תאימות PDF/UA באמצעות ממשק Aspose.PDF API, ייתכן שתרצה לדעת אילו הודעות שגיאה עלולות להתקבל. שגיאות אלו יכולות להיות מסוגים שונים כגון כללי, טקסט, גופנים, כותרות ועוד. מידע על שגיאות כאלה יכול לעזור לדעת את הסיבה המדויקת לשגיאות ואיך לטפל בהן.

במאמר זה, אנו מפרטים את השגיאות שיכולות להתעורר במהלך בדיקת תאימות PDF/UA באמצעות ה-API.

## **כללי**

|**קוד**|**חומרה**|**הודעה**|
| :- | :- | :- |
|5:1|שגיאה|חסר מזהה PDF/UA|
|6.2:1.1|שגיאה|עץ הורה מבני: נמצא רשומה לא עקבית|
|7.1:1.1(14.8.1)|שגיאה|המסמך לא מסומן כמתויג|
|7.1:1.1(14.8)|שגיאה|האובייקט [שם_האובייקט] לא מתויג|
|7.1:1.2(14.8.2.2)|שגיאה|נמצא ארטיפקט בתוך תוכן מתויג|
|7.1:1.3(14.8.2.2)|שגיאה|תוכן מתויג נמצא בתוך ארטיפקט|
|7.1:2.1|אזהרה|עץ המבנה חסר|
|7.1:2.2|אזהרה|נמצא אלמנט מבנה 'מסמך' שאינו אלמנט שורש|
|7.1:2.3|אזהרה|אלמנט מבנה '[שם_האלמנט]' משמש כאלמנט שורש|
|7.1:2.3|אזהרה|השימוש באלמנט מבנה '[ELEMENT_NAME]' כאלמנט השורש|
|7.1:2.4.1|אזהרה|שימוש אפשרי לא ראוי באלמנט מבנה '[ELEMENT_NAME]'|
|7.1:2.4.2|שגיאה|שימוש לא חוקי באלמנט מבנה '[ELEMENT_NAME]'|
|7.1:2.5|אזהרה|שגיאה אפשרית בקינון אלמנט המבנה '[ELEMENT_NAME]' בתוך StructTreeRoot|
|7.1:3(14.8.4)|שגיאה|סוג מבנה לא תקני '[TYPE_NAME]' אינו ממופה לסוג מבנה תקני או לסוג מבנה לא תקני אחר|
|7.1:4(14.8.4)|אזהרה|סוג מבנה תקני '[TYPE_NAME]' ממופה מחדש ל-'[TYPE_NAME]'|
|7.1:5|דרוש בדיקה ידנית|ניגודיות צבעים|
|7.1:6.1|שגיאה|נתוני XMP חסרים במסמך|
|7.1:6.2|שגיאה|הכותרת חסרה בנתוני XMP של המסמך|
|7.1:6.3|אזהרה|הכותרת ריקה בנתוני XMP של המסמך|
|7.1:7.1(12.2)|אזהרה|המילון 'ViewerPreferences' חסר|
|7.1:7.2(12.2)|שגיאה|הכניסה 'DisplayDocTitle' אינה מוגדרת|
|7.1:8(14.7.1)|שגיאה|הכניסה 'Suspects' מוגדרת|
|7.1:9.1(14.7)|שגיאה|המפתח 'StructParents' חסר בדף|
|7.1:9.2(14.7)|שגיאה|הכניסה 'StructParent' חסרה בהערה|
|7.1:9.2(14.7)|Error|חסר רשומת ‘StructParent’ בהערה|
|7.1:9.3(14.7)|Error|לא נמצאה רשומה עבור ‘StructParents’ נתון|

## **Text**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.2:1|Need check manual|סדר קריאה לוגי|
|7.2:2(14.8.2.4.2)|Error|לא ניתן למפות תווים באובייקט טקסט ליוניקוד|
|7.2:3.1(14.9.2.2)|Error|לא ניתן לקבוע שפה טבעית לאובייקט טקסט|
|7.2:3.2(14.9.2.2)|Error|לא ניתן לקבוע שפה טבעית של טקסט חלופי|
|7.2:3.3(14.9.2.2)|Error|לא ניתן לקבוע שפה טבעית של הטקסט הממשי|
|7.2:3.4(14.9.2.2)|Error|לא ניתן לקבוע שפה טבעית של טקסט ההרחבה|
|7.2:4(14.9.4)|Error|תו ניתן למתיחה לא מסומן באמצעות ActualText|

## **Fonts**

|**Clause**|**Severity**|**Message**|
| :- | :- | :- |
|7.21.3.1|Error|אוסף התווים ב-CIDFont אינו תואם לאוסף התווים של ה-CMap הפנימי|
|7.21.3.2|Error|CIDToGIDMap אינו מוטמע או לא שלם בגופן ‘[FONT_NAME]’|
|7.21.3.2|Error|CMap אינו מוטמע עבור גופן ‘[FONT_NAME]’|
|7.21.3.2|שגיאה|CMap אינו מוטמע עבור גופן ‘[FONT_NAME]’|
|7.21.4.2|שגיאה|CIDSet חסר או לא מלא עבור גופן ‘[FONT_NAME]’|
|7.21.4.2|שגיאה|חסרים גליפים בגופן המוטמע ‘[FONT_NAME]’|
|7.21.6|שגיאה|גופן TrueType שאינו סימבולי ‘[FONT_NAME]’ אין לו רשומות cmap|
|7.21.6|שגיאה|רשומת הקידוד אסורה לגופן TrueType סימבולי ‘[FONT_NAME]’|
|7.21.6|שגיאה|שימוש בקידוד שגוי לגופן TrueType ‘[FONT_NAME]’|
|7.21.6|שגיאה|מערך “Differences” שגוי לגופן TrueType שאינו סימבולי ‘[FONT_NAME]’|

## **גרפיקה**

|**קוד**|**חומרה**|**הודעה**|
| :- | :- | :- |
|7.3:1(14.8.4.5)|שגיאה|אלמנט ‘[ELEMENT_NAME]’ בדף יחיד ללא תיבת גבול|
|7.3:2|שגיאה|חסר טקסט חלופי עבור אלמנט מבנה ‘[ELEMENT_NAME]’|
|7.3:3|שגיאה|חסר תיאור לציור שמלווה|
|7.3:4(14.8.4.5)|שגיאה|אובייקט גרפי מופיע בין האופרטורים BT ו-ET|

## **כותרות**

|**קוד**|**חומרה**|**הודעה**|
| :- | :- | :- |
|7.4.2:1|שגיאה|הכותרת הראשונה אינה ברמה הראשונה|
|7.4.2:2|שגיאה|כותרת ממוספרת דילגה על אחת או יותר רמות כותרות|
|7.4.2:2|Error|כותרת ממוספרת דילגה על רמה או יותר של כותרות|
|7.4.4:1|Error|נמצאו אלמנטים מסוג 'H' ו-'Hn'|
|7.4.4:2|Error|יותר מאלמנט 'H' אחד בתוך אלמנט המבנה האב|

## **טבלאות**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.5:1|Warning|שורת טבלה לא סדירה|
|7.5:2|Error|תא כותרת של טבלה ללא תתי תאים מקושרים|
|7.5:3.1|Warning|חסרות כותרות טבלה|
|7.5:3.2|Warning|חסר תקציר טבלה|

## **רשימות**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.6:1|Error|אלמנט מבנה 'LI' חייב להיות ילד של אלמנט 'L'|
|7.6:2|Error|אלמנטי המבנה 'Lbl' ו-'LBody' חייבים להיות ילדים של אלמנט 'LI'|

## **הערות והפניות**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.9:2.1|Error|חסר מזהה באלמנט מבנה 'Note'|
|7.9:2.2|Error|כניסת המזהה באלמנט מבנה 'Note' אינה ייחודית|

## **תוכן אופציונלי**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.10:1|Error|חסר 'Name' במילון הגדרות התוכן האופציונלי|
|7.10:1|Error|חסר 'Name' במילון תצורת התוכן האופציונלי|
|7.10:2|Error|מילון תצורת התוכן האופציונלי מכיל מפתח 'AS'|

## **קבצים מוטבעים**

|**קוד**|**חומרה**|**הודעה**|
| :- | :- | :- |
|7.11:1|Error|חסר מפתח 'F' או 'UF' במפרט הקובץ|
|7.11:2|Warning|חסר מפתח 'Desc' במפרט הקובץ|

## **חתימות דיגיטליות**

|**קוד**|**חומרה**|**הודעה**|
| :- | :- | :- |
|7.13:1|Error|שדה טופס החתימה '[FIELD_NAME]' אינו תואם למפרט|
|7.13:2.1|Error|לא ניתן לקבוע את שפת הממשק הטבעית של שם חלופי של שדה טופס '[FIELD_NAME]'|
|7.13:2.2|Error|חסר רישום שם שדה חלופי בשדה טופס '[FIELD_NAME]'|

## **טפסים שאינם אינטראקטיביים**

|**קוד**|**חומרה**|**הודעה**|
| :- | :- | :- |
|7.14:1|Error|חסר מאפיין 'PrintField' בפריט טופס שאינו אינטראקטיבי|

## **XFA**

|**קוד**|**חומרה**|**הודעה**|
| :- | :- | :- |
|7.15:1|Error|PDF מכיל טופס XFA דינמי|

## **ביטחון**

|**קוד**|**חומרה**|**הודעה**|
|**קוד**|**חומרה**|**הודעה**|
| :- | :- | :- |
|7.16:1(7.6.3.2)|שגיאה|הגדרות האבטחה חוסמות טכנולוגיות עזר לגשת לתוכן המסמך|
|7.16:2(7.6.3.2)|שגיאה|המרה אינה מותרת על ידי הגבלות הרשאות|

## **ניווט**

|**קוד**|**חומרה**|**הודעה**|
| :- | :- | :- |
|7.17:1|שגיאה|שגיאה במתווה המסמכים|
|7.17:2|שגיאה|לא ניתן לקבוע את השפה הטבעית של המתווה|
|7.17:3|דורש בדיקה ידנית|תוויות עמודים בהתאמה סמנטית|

## **הערות**

|**קוד**|**חומרה**|**הודעה**|
| :- | :- | :- |
|7.18.1:1|שגיאה|לא ניתן לקבוע את השפה הטבעית של פריט תוכן|
|7.18.1:2|שגיאה|חסר תיאור חלופי להערה|
|7.18.1:3|שגיאה|ההערה אינה מוטמעת בתוך אלמנט מבנה של 'Annot'|
|7.18.2:1|שגיאה|הערה עם תת-סוג לא מוגדר ב-ISO 32000 אינה עומדת בתקן 7.18.1|
|7.18.2:2|שגיאה|קיימת הערה מסוג TrapNet|
|7.18.3:1|שגיאה|רשומת סדר הכרטיסיות בעמוד עם הערות אינה מוגדרת ל-'S' (מבנה)|
|7.18.4:1|שגיאה|הערת 'Widget' אינה מוטמעת בתוך אלמנט מבנה של 'Form'|

|7.18.4:1|Error|האנוטציה 'Widget' אינה מוטמעת בתוך אלמנט מבנה 'Form'|
|7.18.5:1|Error|האנוטציה 'Link' אינה מוטמעת בתוך אלמנט מבנה 'Link'|
|7.18.6.2:1|Error|מפתח CT חסר ממילון נתוני קליפ מדיה|
|7.18.6.2:2|Error|מפתח Alt חסר ממילון נתוני קליפ מדיה|
|7.18.7:1|Error|אנוטציית קובץ מצורף. חסר מפתח 'F' או 'UF' במפרט הקובץ|
|7.18.7:2|Warning|אנוטציית קובץ מצורף. חסר מפתח 'Desc' במפרט הקובץ|
|7.18.8:1|Error|אנוטציית PrinterMark כלולה במבנה לוגי|
|7.18.8:2|Error|זרם ההופעה של אנוטציית PrinterMark אינו מסומן כארטיפקט|

## **Actions**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.19:1|Need check manual|נמצאו פעולות. יש לבדוק את הפעולות על פי המפרט PDF/UA באופן ידני|

## **XObjects**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.20:1|Error|אין להשתמש ב-XObject המפנה בקובץ PDF/UA תואם|
|7.20:2|Error|תוכן של Form XObject אינו מוטמע באלמנטי מבנה|
|7.20:2|שגיאה|תוכן של Form XObject אינו משולב באלמנטים מובנים

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

