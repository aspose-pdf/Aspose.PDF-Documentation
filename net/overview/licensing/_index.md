---
title: Aspose PDF License
linktitle: Licensing and limitations
type: docs
weight: 50
url: /net/licensing/
description: Aspose. PDF for .NET invites its customers to get a Classic license and Metered License. As well as use a limited license to better explore the product.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Limitation of an evaluation version

We want our customers to test our components thoroughly before buying so the evaluation version allows you to use it as you would normally.

- **PDF created with an evaluation watermark.** The evaluation version of Aspose.PDF for .NET provides full product functionality, but all the pages in the generated PDF documents are watermarked with "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" at the top.

- **The limit of the number of collection items that can be processed.**
In the evaluation version from any collection, you can process only four elements (for example, only 4 pages, 4 form fields, etc.).

>If you want to test Aspose.HTML for .NET without the evaluation version limitations, you can also request a 30-day Temporary License. Please refer to [How to get a Temporary License?](https://purchase.aspose.com/temporary-license)

## Classic license

The license can be loaded from a file or stream object. The easiest way to set a license is to put the license file in the same folder as the Aspose.PDF.dll file and specify the file name without a path, as shown in the example below.

If you use any other Aspose for .NET component along with Aspose.PDF for .NET, please specify the namespace for License like [Aspose.Pdf.License](https://reference.aspose.com/pdf/net/aspose.pdf/license).

### Loading a license from file

The easiest way to apply a license is to put the license file in the same folder as the Aspose.PDF.dll file and specify just the file name without a path.

When you call the [SetLicense](https://reference.aspose.com/pdf/net/aspose.pdf/license/methods/setlicense/index) method, the license name that you pass should be that of your license file. For example, if you change the license file name to "Aspose.PDF.lic.xml" pass that file name to the Pdf.SetLicense(…) method.

```csharp

public static void SetLicenseExample()
{
    // Initialize license object
    Aspose.Pdf.License license = new Aspose.Pdf.License();
    try
    {
        // Set license
        license.SetLicense("Aspose.Pdf.lic");
    }
    catch (Exception)
    {
        // something went wrong
        throw;
    }
    Console.WriteLine("License set successfully.");
}
```
### Loading the license from a stream object

The following example shows how to load a license from a stream.

```csharp
public static void SetLicenseFromStream()
{
    // Initialize license object
    Aspose.Pdf.License license = new Aspose.Pdf.License();
    // Load license from the file stream
    System.IO.FileStream myStream =
        new System.IO.FileStream(
            "Aspose.Pdf.lic",
            System.IO.FileMode.Open);
    // Set license
    license.SetLicense(myStream);
    Console.WriteLine("License set successfully.");
}
```
## Metered License

Aspose.PDF allows developers to apply metered key. It is a new licensing mechanism. The new licensing mechanism will be used along with existing licensing method. Those customers who want to be billed based on the usage of the API features can use the metered licensing. For more details, please refer to Metered Licensing FAQ section.

A new class Metered has been introduced to apply metered key. Following is the sample code demonstrating how to set metered public and private keys.

 For more details, please refer to the [Metered Licensing FAQ](https://purchase.aspose.com/faqs/licensing/metered) section.

```csharp
public static void SetMeteredLicense()
{
    // set metered public and private keys
    Aspose.Pdf.Metered metered = new Aspose.Pdf.Metered();
    // Access the setMeteredKey property and pass public and private keys as parameters
    metered.SetMeteredKey(
        "<type public key here>",
        "<type private key here>");

    // Load the document from disk.
    Document doc = new Document("input.pdf");
    //Get the page count of document
    Console.WriteLine(doc.Pages.Count);
}
```

Please note that COM applications that work with **Aspose.PDF for .NET** should also use the License class.

One point which needs consideration:
Please note that the embedded resources are included in assembly the way they are added i.e. if you add text file as an embedded resource in the application and open the resultant EXE in notepad, you will see the exact contents of text file. So when using license file as an embedded resource, anyone can open exe file in some simple text editor and see/extract the contents of embedded license.

Therefore, in order to put an extra layer of security when embedding the license with the application, you can compress/encrypt license and after that, you can embed it into the assembly. Suppose we have Aspose.PDF.lic license file, so let's make Aspose.PDF.zip with password test and embed this zip file into solution. The following code snippet can be used to initialize the license:

```csharp
using System;
using System.IO;
using System.IO.Compression;
using System.Reflection;

namespace Aspose.Pdf.Examples
{
    class ExampleLicensing
    {
        public static void LicenseDemo()
        {
            License license = new License();
            license.SetLicense(GetSecureLicenseFromStream());
            Document doc = new Document("document.pdf");
            //Get the page count of document
            Console.WriteLine(doc.Pages.Count);
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
    }
}
```
### Applying a License Bought Before 2005/01/22

Aspose.PDF for .NET no longer supports the old-style licenses. If you have a license from before 22 January 2005 and you have updated to a more recent version of Aspose.PDF, please contact our Sales team to get a new license file.
