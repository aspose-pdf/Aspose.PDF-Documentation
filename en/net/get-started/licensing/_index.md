---
title: Aspose PDF License
linktitle: Licensing and limitations
type: docs
weight: 90
url: /net/licensing/
description: Aspose. PDF for .NET invites its customers to get a Classic license and Metered License. As well as use a limited license to better explore the product.
lastmod: "2025-02-07"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Aspose PDF for .NET License",
    "alternativeHeadline": "Licensing Options for Aspose.PDF for .NET Users",
    "abstract": "Aspose PDF for .NET introduces a robust licensing framework including both Classic and Metered licenses, allowing users to choose between fixed pricing and usage-based billing options. The Classic license can be easily loaded from a file or stream, while the innovative Metered license provides flexible metering based on API usage, catering to diverse user needs. This dual licensing strategy enhances the accessibility and scalability of PDF solutions for developers",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "869",
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
    "url": "/net/licensing/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/licensing/"
    },
    "dateModified": "2025-02-07",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Limitation of an evaluation version

We want our customers to test our components thoroughly before buying so the evaluation version allows you to use it as you would normally.

- **PDF created with an evaluation watermark.** The evaluation version of Aspose.PDF for .NET provides full product functionality, but all pages in the generated PDF documents are watermarked with the text "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2025 Aspose Pty Ltd." at the top.

- **Limit the number of pages that can be processed.**
In the evaluation version, you can only process the first four pages of a document.

>If you want to test Aspose.PDF for .NET without the evaluation version limitations, you can also request a 30-day Temporary License. Please refer to [How to get a Temporary License?](https://purchase.aspose.com/temporary-license)

## Classic license

The license can be loaded from a file or stream object. The easiest way to set a license is to put the license file in the same folder as the Aspose.PDF.dll file and specify the file name without a path, as shown in the example below.

If you use any other Aspose for .NET component along with Aspose.PDF for .NET, please specify the namespace for License like [Aspose.Pdf.License](https://reference.aspose.com/pdf/net/aspose.pdf/license).

### Loading a license from file

The easiest way to apply a license is to put the license file in the same folder as the Aspose.PDF.dll file and specify just the file name without a path.

When you call the [SetLicense](https://reference.aspose.com/pdf/net/aspose.pdf/license/methods/setlicense/index) method, the license name that you pass should be that of your license file. For example, if you change the license file name to "Aspose.PDF.lic.xml" pass that file name to the Pdf.SetLicense(…) method.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseExample()
{
    // Initialize license object
    var license = new Aspose.Pdf.License();
    try
    {
        // Set license
        license.SetLicense("Aspose.Pdf.lic");
    }
    catch (Exception)
    {
        // Something went wrong
        throw;
    }
    Console.WriteLine("License set successfully.");
}
```
### Loading the license from a stream object

The following example shows how to load a license from a stream.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseFromStream()
{
    // Initialize license object
    var license = new Aspose.Pdf.License();
    // Load license from the file stream
    var myStream = new FileStream(
            "Aspose.Pdf.lic",
            FileMode.Open);
    // Set license
    license.SetLicense(myStream);
    Console.WriteLine("License set successfully.");
}
```
## Metered License

Aspose.PDF allows developers to apply metered key. The metered licensing mechanism will be used along with existing licensing method. Those customers who want to be billed based on the usage of the API features can use the metered licensing. For more details, please refer to Metered Licensing FAQ section.
This guide provides best practices for smooth implementation and preventing disruptions due to licensing status changes.

The class "Metered" is used to apply metered keys. Following is the sample code demonstrating how to set metered public and private keys.

For more details, please refer to the [Metered Licensing FAQ](https://purchase.aspose.com/faqs/licensing/metered) section.

__Metered Licensing Methods__

Applying the Metered License use the `SetMeteredKey` method to activate the metered license by providing your public and private keys. This should be done once during application initialization to ensure proper licensing.

Example: 

```csharp
 var metered = new Aspose.Pdf.Metered();
 metered.SetMeteredKey("your-public-key", "your-private-key");
 ```
Checking License Status uses `IsMeteredLicensed()` to verify if the metered license is active.

Example:

```csharp
bool isLicensed = Aspose.Pdf.License.IsMeteredLicensed();
if (!isLicensed) 
{
    metered.SetMeteredKey("your-public-key", "your-private-key");
}
 ```
The method `Metered.GetConsumptionCredit()` is used to get the information about consumption credits.
The method `Metered.GetConsumptionQuantity()` is used to get the information about consumption file size.

Example:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetMeteredLicense()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    // Set metered public and private keys
    var metered = new Aspose.Pdf.Metered();
    // Access the setMeteredKey property and pass public and private keys as parameters
    metered.SetMeteredKey("your public key", "your private key");

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
       // Add five pages
       AddPages(document, 5);
       // Save the document
       document.Save(dataDir + "output.pdf")
    }
}

private static void AddPages(Document document, int n)
{
    for(int i = 0; i < n; i++)
    {
        document.Pages.Add();
    }
}   
```

__Best Practices for Metered Licensing__

✅ Recommended Approach: Singleton Pattern
To ensure a stable licensing setup:

- Apply the license once at application startup.
- Use a singleton pattern (or similar approach) to create and reuse the metered license instance.
- Periodically check the license status using `IsMeteredLicensed()`. Reapply the license only if it becomes invalid.
- If implemented correctly, the license remains valid for 24 hours even if the license server is temporarily unavailable.

Example: Singleton Implementation

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
public class AsposeLicenseManager
{
    private static AsposeLicenseManager _instance;
    private static readonly object _lock = new object();
    private Aspose.Pdf.Metered _metered;

    private AsposeLicenseManager()
    {
        _metered = new Aspose.Pdf.Metered();
        _metered.SetMeteredKey("your-public-key", "your-private-key");
    }

    public static AsposeLicenseManager Instance
    {
        get
        {
            lock (_lock)
            {
                if (_instance == null)
                {
                    _instance = new AsposeLicenseManager();
                }
                return _instance;
            }
        }
    }

    public void ValidateLicense()
    {
        if (!Aspose.Pdf.License.IsMeteredLicensed())
        {
        _metered.SetMeteredKey("your-public-key", "your-private-key");
        }
    }
}
```

❌ Common Mistakes to Avoid:

- Frequent License Applications
- Do not create a new metered license instance for every operation.
- If the license server is unreachable during initialization, the license may revert to evaluation mode.
- Do not apply the license repeatedly for each operation.
- Frequent license applications can cause fallback into trial mode if the license server is temporarily unavailable.

__Summary:__

✅ Set the metered license once at application startup.
✅ Use a singleton pattern to manage a single instance.
✅ Periodically check and reapply the license if needed.
❌ Avoid frequent license applications to prevent trial mode fallback.
By following these best practices, you ensure smooth and uninterrupted usage of Aspose.PDF with metered licensing.

If the license was initialized, then as long as this object "lives", even if the connection to the license server is lost for some reason, the license will be considered active for another 7 days. If you initialize a license whenever you need to do something and there is no connection to the server at the moment of initialization, then the license will go into Eval mode.
It should be additionally emphasized that if a user has initialized a license, then as long as this object "lives", even if the connection to the license server is lost for some reason, the license will be considered active for another 24 hours. If you initialize a license whenever you need to do something and there is no connection to the server at the moment of initialization, then the license will go into Eval mode.

Please note that COM applications that work with **Aspose.PDF for .NET** should also use the License class.

One point which needs consideration:
Please note that the embedded resources are included in assembly the way they are added i.e. if you add text file as an embedded resource in the application and open the resultant EXE in notepad, you will see the exact contents of text file. So when using license file as an embedded resource, anyone can open exe file in some simple text editor and see/extract the contents of embedded license.

Therefore, in order to put an extra layer of security when embedding the license with the application, you can compress/encrypt license and after that, you can embed it into the assembly. Suppose we have Aspose.PDF.lic license file, so let's make Aspose.PDF.zip with password test and embed this zip file into solution. The following code snippet can be used to initialize the license:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseFromStream()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    var license = new Aspose.Pdf.License();
    license.SetLicense(GetSecureLicenseFromStream());
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the page count of document
        Console.WriteLine(document.Pages.Count);
    }
}

private static Stream GetSecureLicenseFromStream()
{
    var assembly = Assembly.GetExecutingAssembly();
    var memoryStream = new MemoryStream();
    using (var zipToOpen = assembly.GetManifestResourceStream("Aspose.Pdf.Examples.License.Aspose.PDF.zip"))
    {
        using (ZipArchive archive = new ZipArchive(zipToOpen ?? throw new InvalidOperationException(), ZipArchiveMode.Read))
        {
            var unpackedLicense  = archive.GetEntry("Aspose.PDF.lic");
            unpackedLicense?.Open().CopyTo(memoryStream);
        }
    }

    memoryStream.Position = 0;
    return memoryStream;
}
```

