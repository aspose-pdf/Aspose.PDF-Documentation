---
title: הוספת תמונה לקובץ PDF באמצעות C#
linktitle: הוספת תמונה
type: docs
weight: 10
url: /net/add-image-to-existing-pdf-file/
description: פרק זה מתאר איך להוסיף תמונה לקובץ PDF קיים באמצעות ספריית C#.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "הוספת תמונה לקובץ PDF באמצעות C#",
    "alternativeHeadline": "איך להוסיף תמונה לקובץ PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, הוספת תמונה ל-pdf",
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
    "url": "/net/add-image-to-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-image-to-existing-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "פרק זה מתאר איך להוסיף תמונה לקובץ PDF קיים באמצעות ספריית C#."
}
</script>
## הוספת תמונה בקובץ PDF קיים

כל דף PDF מכיל את המאפיינים משאבים ותוכן. משאבים יכולים להיות תמונות וטפסים לדוגמה, בעוד שהתוכן מיוצג על ידי קבוצת אופרטורים של PDF. לכל אופרטור יש שם וארגומנט. הדוגמה הזו משתמשת באופרטורים כדי להוסיף תמונה לקובץ PDF.

הקטע קוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

כדי להוסיף תמונה לקובץ PDF קיים:

- צור אובייקט מסמך ופתח את מסמך ה-PDF הנכנס.
- קבל את הדף שבו ברצונך להוסיף תמונה.
- הוסף את התמונה לאוסף המשאבים של הדף.
- השתמש באופרטורים כדי למקם את התמונה בדף:
- השתמש באופרטור GSave כדי לשמור את מצב הגרפיקה הנוכחי.
- השתמש באופרטור ConcatenateMatrix כדי לציין איפה התמונה תמוקם.
- השתמש באופרטור Do כדי לצייר את התמונה בדף.
- לבסוף, השתמש באופרטור GRestore כדי לשמור את מצב הגרפיקה המעודכן.
- שמור את הקובץ.
הקטע הבא מראה איך להוסיף את התמונה במסמך PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקרו ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// פתח מסמך
Document pdfDocument = new Document(dataDir+ "AddImage.pdf");

// קבע קואורדינטות
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// קבל את הדף שבו יש להוסיף תמונה
Page page = pdfDocument.Pages[1];
// טען תמונה לתוך זרם
FileStream imageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open);
// הוסף תמונה לאוסף התמונות של משאבי הדף
page.Resources.Images.Add(imageStream);
// באמצעות אופרטור GSave: אופרטור זה שומר את מצב הגרפיקה הנוכחי
page.Contents.Add(new Aspose.Pdf.Operators.GSave());
// צור אובייקטים מלבן ומטריצה
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY });
// באמצעות ConcatenateMatrix (מטריצת שרשור) אופרטור: מגדיר איך תמונה צריכה להיות מונחת
page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
XImage ximage = page.Resources.Images[page.Resources.Images.Count];
// באמצעות אופרטור Do: אופרטור זה מצייר תמונה
page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
// באמצעות אופרטור GRestore: אופרטור זה שוחזר מצב גרפיקה
page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
dataDir = dataDir + "AddImage_out.pdf";
// שמור מסמך מעודכן
pdfDocument.Save(dataDir);
```
{{% alert color="primary" %}}

כברירת מחדל, איכות ה-JPEG מוגדרת ל-100%. להחיל דחיסה ואיכות טובות יותר, השתמש בהעמסות הבאות:

{{% /alert %}}

- נוספה טעינה מחדש של המתודה Replace למחלקת XImageCollection: public void Replace(int index, Stream stream, int quality)
- נוספה טעינה מחדש של המתודה Add למחלקת XImageCollection: public void Add(Stream stream, int quality)

## הוספת תמונה בקובץ PDF קיים (Facades)

קיימת גם דרך חלופית וקלה יותר להוסיף תמונה לקובץ PDF.
יש גם דרך חלופית וקלה יותר להוסיף תמונה לקובץ PDF.

```csharp
string imageFileName = Path.Combine(_dataDir, "Images", "Sample-01.jpg");
string outputPdfFileName = Path.Combine(_dataDir, "Example-add-image-mender.pdf");
Document document = new Document();
Page page = document.Pages.Add();
page.SetPageSize(PageSize.A3.Height, PageSize.A3.Width);
page = document.Pages.Add();
Aspose.Pdf.Facades.PdfFileMend mender = new Aspose.Pdf.Facades.PdfFileMend(document);
mender.AddImage(imageFileName, 1, 0, 0, (float)page.CropBox.Width, (float)page.CropBox.Height);
document.Save(outputPdfFileName);
```

## שים תמונה על הדף ושמור (שליטה) על יחס הממדים

אם אנו לא יודעים את ממדי התמונה יש סיכוי לקבל תמונה מעוותת על הדף. הדוגמה הבאה מראה אחת הדרכים להימנע מכך.

```csharp
public static void AddingImageAndPreserveAspectRatioIntoPDF()
{
    var bitmap = System.Drawing.Image.FromFile(_dataDir + "3410492.jpg");

    int width;
    int height;

    width = bitmap.Width;
    height = bitmap.Height;

    var document = new Aspose.Pdf.Document();

    var page = document.Pages.Add();

    int scaledWidth = 400;
    int scaledHeight = scaledWidth * height / width;

    page.AddImage(_dataDir + "3410492.jpg", new Aspose.Pdf.Rectangle(10, 10, scaledWidth, scaledHeight));
    document.Save(_dataDir + "sample_image.pdf");
}
```
## זיהוי אם תמונה בקובץ PDF היא צבעונית או שחור-לבן

סוגים שונים של דחיסה יכולים להיות מוחלים על תמונות כדי להקטין את גודלן. סוג הדחיסה שמוחל על תמונה תלוי במרחב הצבעים של התמונה המקורית, כלומר אם התמונה היא צבעונית (RGB), יש להחיל דחיסת JPEG2000, ואם היא שחור-לבן, יש להחיל דחיסת JBIG2/JBIG2000. לכן, זיהוי סוג התמונה ושימוש בסוג הדחיסה המתאים יוצרים תוצאה מיטבית/מוטבת.

קובץ PDF עשוי להכיל טקסט, תמונה, גרף, קובץ מצורף, הערה וכו' ואם קובץ PDF המקורי מכיל תמונות, אנו יכולים לקבוע את מרחב הצבע של התמונה ולהחיל דחיסה מתאימה על התמונה כדי להקטין את גודל קובץ ה-PDF. קטע הקוד הבא מראה את השלבים לזיהוי אם תמונה ב-PDF היא צבעונית או שחור-לבן.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// מונה לתמונות בגרייסקייל
int grayscaled = 0;
// מונה לתמונות RGB
int rgd = 0;

using (Document document = new Document(dataDir + "ExtractImages.pdf"))
{
    foreach (Page page in document.Pages)
    {
        Console.WriteLine("--------------------------------");
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
        page.Accept(abs);
        // קבלת מספר התמונות בעמוד ספציפי
        Console.WriteLine("Total Images = {0} over page number {1}", abs.ImagePlacements.Count, page.Number);
        // Document.Pages[29].Accept(abs);
        int image_counter = 1;
        foreach (ImagePlacement ia in abs.ImagePlacements)
        {
            ColorType colorType = ia.Image.GetColorType();
            switch (colorType)
            {
                case ColorType.Grayscale:
                    ++grayscaled;
                    Console.WriteLine("Image {0} is GrayScale...", image_counter);
                    break;
                case ColorType.Rgb:
                    ++rgd;
                    Console.WriteLine("Image {0} is RGB...", image_counter);
                    break;
            }
            image_counter += 1;
        }
    }
}
```
## שליטה באיכות התמונה

ניתן לשלוט באיכות של תמונה שמתווספת לקובץ PDF. השתמש במתודה העמוסה [Replace](https://reference.aspose.com/pdf/net/aspose.pdf.ximagecollection/replace/methods/1) במחלקה [XImageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/ximagecollection).

הקטע קוד הבא מדגים כיצד להמיר את כל תמונות המסמך ל-JPEGs שמשתמשות באיכות של 80% לדחיסה.

```csharp
Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document(inFile);
foreach (Aspose.PDF.Page page in pdfDocument.Pages)
{
    int idx = 1;
    foreach (Aspose.PDF.XImage image in page.Resources.Images)
    {
        using (MemoryStream imageStream = new MemoryStream())
        {
            image.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
            page.Resources.Images.Replace(idx, imageStream, 80);
            idx = idx + 1;
        }
    }
}

// pdfDocument.OptimizeResources();

pdfDocument.Save(outFile);
```

<script type="application/ld+json">

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
                "contactType": "מכירות",
                "areaServed": "ארה\"ב",
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "מכירות",
                "areaServed": "בריטניה",
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "מכירות",
                "areaServed": "אוסטרליה",
                "availableLanguage": "אנגלית"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "ספריית עיבוד PDF ל-.NET",
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

