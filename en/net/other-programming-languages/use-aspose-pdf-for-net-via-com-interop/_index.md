---
title: Aspose.PDF for .NET via COM Interop
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /net/use-aspose-pdf-for-net-via-com-interop/
description: Discover how to use Aspose.PDF for .NET via COM Interop for seamless integration with non-.NET applications.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Aspose.PDF for .NET via COM Interop",
    "alternativeHeadline": "Aspose.PDF for .NET Enables COM Interop Usage",
    "abstract": "Aspose.PDF for .NET now supports seamless integration with various programming languages through COM Interop, allowing developers to utilize its powerful PDF manipulation capabilities outside the .NET framework. This feature enhances flexibility by transforming Aspose.PDF objects into COM objects, streamlining interactions with unmanaged code while maintaining high performance through early and late binding techniques",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1338",
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
    "url": "/net/use-aspose-pdf-for-net-via-com-interop/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/use-aspose-pdf-for-net-via-com-interop/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

{{% alert color="primary" %}}

The information in this topic applies to scenarios where you want to use [Aspose.PDF for .NET](/pdf/net/) via COM Interop in any of the following programming languages:

- ASP
- Delphi
- JScript
- Perl
- PHP
- PowerBuilder
- Python
- VBScript
- Visual Basic
- C++

{{% /alert %}}

## Working with COM Interop

Aspose.PDF for .NET executes under the control of the .NET Framework and this is called managed code. Code written in all of the above languages runs outside the .NET Framework and it is called unmanaged code. Interaction between unmanaged code and Aspose.PDF occurs via the .NET facility called COM Interop.

Aspose.PDF objects are .NET objects, but when used via COM Interop, they appear as COM objects in your programming language. Therefore, it is best to make sure you know how to create and use COM objects in your programming language, before you start using [Aspose.PDF for .NET](/pdf/net/).

{{% alert color="primary" %}}

- In COM world we distinguish COM server and COM client. COM server stored COM classes while COM client asks COM server for classes instances, i.e. COM objects.
- COM client or simply client application can know about COM class contents something or be totally unaware about its methods and properties. Therefore client application can discover COM class structure on compiling/building or only during execution. Process of "discovery" is known as binding and so we have **early binding** and **late binding**.
- in brief COM class is like black box and to work with it type library is needed, this binary file has description of COM class methods, properties and any high level language which supports working with COM objects often has syntax expression for adding type library, for instance this is [**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx) in C++.
- type library is used for early binding.
- a COM object can expose its methods and properties in two ways: by means of a **dispatch interface** (dispinterface) and in its **vtable** (virtual function table).
- within the **dispinterface**, each method and property is identified by a unique member; this member is the function's dispatch identifier(or **DispID**).
- **vtable** is just a set of pointers to functions that the COM class interface supports.
- an object that exposes its methods through both interfaces supports a **dual interface**.
- there are advantages to both types of binding. Early binding provides you with increased performance and compile-time syntax checking. Late binding is most advantageous when you are writing clients that you intend to be ***compatible with future versions*** of your COM class. With late binding, information from the type library is not "hard-wired" into your client, so you can have greater confidence that your client can work with future versions of COM class without code changes.
- late binding mechanism has a big advantage: if the creator of the COM DLL decides to release a new version, with a different function interface layout, any code calling those methods won't crash unless the methods are no longer available; even if the **vtable** is different late binding manages to discover the new DISPIDs and call appropriate methods.
{{% /alert %}}

Here are the topics that you will eventually need to master:
{{% alert color="primary" %}}

- Using COM objects in your programming language. See your programming language documentation and the language-specific topics further in this documentation.

- Working with COM objects exposed by .NET COM Interop. See [Interoperating With Unmanaged Code](http://msdn.microsoft.com/en-us/library/sd10k43k.aspx) and [Exposing .NET Framework Components to COM](http://msdn.microsoft.com/en-us/library/zsfww439%28v=vs.110%29.aspx) in MSDN.

- Aspose.PDF document object model. See [Aspose.PDF Programmer's Guide](http://www.aspose.com/docs/display/pdfnet/Programmers+Guide) and [API Reference](http://www.aspose.com/docs/display/pdfnet/Aspose.PDF+for+.NET+API+Reference).

{{% /alert %}}

## Register Aspose.PDF for .NET with COM Interop

You need to install Aspose.PDF for .NET and make sure it is registered with COM Interop (ensuring that it can be called from unmanaged code).

{{% alert color="primary" %}}

To register Aspose.PDF for .NET for COM Interop manually:

1. From the **Start** menu, select **All Programs**, then **Microsoft Visual Studio**, **Visual Studio Tools** and, finally, **Visual Studio Command Prompt**.
1. Enter the command to register the assembly:
   1. .NET Framework 4.8.1
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.dll" /codebase
   1. .NET 6.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.dll" /codebase
   1. .NET 7.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.dll" /codebase
   1. .NET 8.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.dll" /codebase
   1. .NET Standard 2.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.dll" /codebase

{{% /alert %}}

Pay attention that /codebase is necessary only if Aspose.PDF.dll is not in GAC, using this option makes regasm put path for assembly in registry.

{{% alert color="primary" %}}

regasm.exe is a tool included in .NET Framework SDK. All the .NET Framework SDK tools are located in the *\Microsoft .NET\Framevork\<FrameworkVersion>* directory, for example *C:\Windows\Microsoft .NET\Framework\v4.0.30319*. If you use Visual Studio .NET:
From the **Start** menu, select **Programs**, followed by **Visual Studio 2022**, finally, **Developer Command Prompt for VS 2022**.
It runs a command prompt with all the necessary environment variables set.

{{% /alert %}}

### ProgIDs

ProgID stands for “programmatic identifier”. It is the name of a COM class that used to create an object. ProgIDs consist of the library name "Aspose.PDF" and the class name.

### Type Library

{{% alert color="primary" %}}

If your programming language (for example Visual Basic or Delphi) allows you to reference a COM type library, then add a reference to Aspose.PDF.tlb and to see all Aspose.PDF for .NET classes, methods, properties and enumerations in your Object Browser.

To generate a TLB file:

- .NET Framework 4.8.1
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.tlb" /codebase
- .NET 6.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.tlb" /codebase
- .NET 7.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.tlb" /codebase
- .NET 8.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.tlb" /codebase
- .NET Standard 2.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.tlb" /codebase

{{% /alert %}}

## Creating COM Objects

The creation of a COM object is similar to creation of a normal .NET object:

```vb
'Instantiate Pdf instance by calling its empty constructor
Dim document
Set document = CreateObject("Aspose.Pdf.Document")

```

Once created, you are able to access the object's methods and properties, as if it was a COM object:

```vb
'Add page to the document
document.Pages.Add()
```

Some methods have overloads and they will be exposed by COM Interop with a numeric suffix added to them, except for the very first method that stays unchanged. For example, the Document.Save method overloads become Document.Save, Document.Save_2, and so on.

For more information, see the language-specific articles further in this documentation.

## Creating a Wrapper Assembly

If you need to use many of Aspose.PDF for .NET classes, methods and properties, consider creating a wrapper assembly (using C# or any other .NET programming language). Wrapper assemblies help help to avoid using Aspose.PDF for .NET directly from unmanaged code.

A good approach is to develop a .NET assembly that references Aspose.PDF for .NET and does all the work with it, and only exposes a minimal set of classes and methods to unmanaged code. Your application then should work just with your wrapper library.

Reducing the number of classes and methods that you need to invoke via COM Interop simplifies the project. Using .NET classes via COM Interop often requires advanced skills.
