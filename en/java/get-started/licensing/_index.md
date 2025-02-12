---
title: Licensing and limitations
linktitle: Licensing and limitations
type: docs
weight: 90
url: /java/licensing/
description: Aspose.PDF for Java invites its customers to get a Classic license and Metered License. As well as use a limited license to better explore the product.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Overview of Evaluation and Licensing of the Aspose.PDF for Java
Abstract: The article provides a comprehensive overview of the evaluation and licensing options available for Aspose.PDF for Java. It details the limitations of the evaluation version, which includes watermarked PDFs and a restriction on processing only four collection items. Users are encouraged to thoroughly test the product, with options to purchase a license or request a 30-day temporary license for full functionality without restrictions. The article explains how to load a classic license from a file or stream and emphasizes the importance of setting a license before document operations. Additionally, it introduces the metered license option for usage-based billing, with guidance on applying metered keys. For users employing multiple Aspose products, the article advises setting licenses separately for each product and using fully qualified class names to avoid confusion. Code examples are provided throughout to illustrate the licensing process.
SoftwareApplication: java
---

## Limitation of an evaluation version

We want our customers to test our components thoroughly before buying so the evaluation version allows you to use it as you would normally.

- **PDF created with an evaluation watermark.** The evaluation version of Aspose.PDF for Java provides full product functionality, but all the pages in the generated PDF documents are watermarked with "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" at the top.

- **The limit of the number of collection items that can be processed.**
In the evaluation version from any collection, you can process only four elements (for example, only 4 pages, 4 form fields, etc.).

You can download an evaluation version of **Aspose.PDF** for Java from [Aspose Repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). The evaluation version provides absolutely the same capabilities as the licensed version of the product. Furthermore, evaluation version simply becomes licensed when you purchase a license and add a couple of lines of code to apply the license.

Once you are happy with your evaluation of **Aspose.PDF**, you can [purchase a license](https://purchase.aspose.com/) at the Aspose website. Make yourself familiar with the different subscription types offered. If you have any questions, do not hesitate to contact the Aspose sales team.

Every Aspose license carries a one-year subscription for free upgrades to any new versions or fixes that come out during this time. Technical support is free and unlimited and provided both to licensed and evaluation users.

>If you want to test Aspose.PDF for Java without the evaluation version limitations, you can also request a 30-day Temporary License. Please refer to [How to get a Temporary License?](https://purchase.aspose.com/temporary-license)

## Classic license

The license can be loaded from a file or stream object. The easiest way to set a license is to put the license file in the same folder as the Aspose.PDF.dll file and specify the file name without a path, as shown in the example below.

The license is a plain text XML file that contains details such as the product name, number of developers it is licensed to, subscription expiry date and so on. The file is digitally signed, so do not modify the file; even the inadvertent addition of an extra line break into the file will invalidate it.

You need to set a license before performing any operations with documents. You are only required to set a license once per application or process.

The license can be loaded from a stream or file in the following locations:

1. Explicit path.
1. The folder that contains the aspose-pdf-xx.x.jar.

Use the License.setLicense method to license the component. Often the easiest way to set a license is to put the license file in the same folder as Aspose.PDF.jar and specify just the file name without path as shown in the following example:

{{% alert color="primary" %}}

Starting from Aspose.PDF for Java 4.2.0, you need to call the following code lines to initialize the license.

{{% /alert %}}

### Loading a license from file

In this example **Aspose.PDF** will attempt to find the license file in the folder that contain the JARs of your application.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Call setLicense method to set license
license.setLicense("Aspose.Pdf.Java.lic");
```
### Loading the license from a stream object

The following example shows how to load a license from a stream.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set license from Stream
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```
#### Setting a License Purchased Before 2005/01/22
**Aspose.PDF** for Java doesn't support old licenses anymore so please contact our [sales team](https://company.aspose.com/contact) to get new license file.

### Validate the License

It is possible to validate if the license has been set properly or not. The Document class has the isLicensed method that will return true if license has been properly set.

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Check if license has been validated
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```
## Metered License

Aspose.PDF allows developers to apply metered key. It is a new licensing mechanism. The new licensing mechanism will be used along with existing licensing method. Those customers who want to be billed based on the usage of the API features can use the metered licensing. For more details, please refer to [Metered Licensing FAQ](https://purchase.aspose.com/faqs/licensing/metered) section.

A new class [Metered](https://reference.aspose.com/pdf/java/com.aspose.pdf/Metered) has been introduced to apply metered key. Following is the sample code demonstrating how to set metered public and private key.

```java
String publicKey = "";
String privateKey = "";

Metered m = new Metered();
m.setMeteredKey(publicKey, privateKey);

// Optionally, the following two lines returns true if a valid license has been applied;
// false if the component is running in evaluation mode.
License lic = new License();
System.out.println("License is set = " + lic.isLicensed());
```
## Using Multiple Products from Aspose

If you use multiple Aspose products in your application, for example Aspose.PDF and Aspose.Words, here are a few useful tips.

- **Set the License for each Aspose Product Separately.** Even if you have a single license file for all components, for example 'Aspose.Total.lic', you still need to call **License.SetLicense** separately for each Aspose product you are using in your application.
- **Use Fully Qualified License Class Name.** Each Aspose product has a **License** class in its namespace. For example, Aspose.PDF has **com.aspose.pdf.License** and Aspose.Words has **com.aspose.words.License** class. Using the fully qualified class name allows you to avoid any confusion about which license is applied to which product.

```java
// Instantiate the License class of Aspose.Pdf
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set the license
license.setLicense("Aspose.Total.Java.lic");

// Setting license for Aspose.Words for Java

// Instantiate the License class of Aspose.Words
com.aspose.words.License licenseaw = new com.aspose.words.License();
// Set the license
licenseaw.setLicense("Aspose.Total.Java.lic");
```