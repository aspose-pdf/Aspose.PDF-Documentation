---
title: Travailler avec JavaScript
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 120
url: /fr/net/working-with-javascript/
description: Apprenez à ajouter, modifier et exécuter JavaScript dans des documents PDF en utilisant Aspose.PDF for .NET. Améliorez l'interactivité et l'automatisation.
lastmod: "2025-02-07"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with JavaScript",
    "alternativeHeadline": "Enhance PDF with Custom JavaScript Actions",
    "abstract": "Découvrez les capacités améliorées d'intégration de JavaScript dans des documents PDF grâce à Aspose.PDF for .NET. Cette nouvelle fonctionnalité permet aux développeurs d'ajouter et de gérer des actions JavaScript à la fois au niveau du document et de la page, permettant des expériences PDF interactives et dynamiques visant à améliorer l'engagement et la fonctionnalité des utilisateurs. Débloquez le potentiel de JavaScript pour créer des formulaires PDF sophistiqués qui imitent des comportements similaires à ceux du Web, élevant vos flux de travail de génération de documents.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "JavaScript, Acrobat JavaScript, PDF document generation, JavaScript collection, document level JavaScript, JavaScript Action, interactive PDF forms, manipulate PDF files, HTML JavaScript, Aspose.PDF for .NET",
    "wordcount": "423",
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
    "url": "/net/working-with-javascript/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-javascript/"
    },
    "dateModified": "2025-02-07",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

## Ajouter JavaScript (DOM)

### Qu'est-ce qu'Acrobat JavaScript ?

Acrobat JavaScript est un langage basé sur le noyau de JavaScript version 1.5 de l'ISO-16262, anciennement connu sous le nom d'ECMAScript, un langage de script orienté objet développé par Netscape Communications. JavaScript a été créé pour décharger le traitement des pages Web d'un serveur vers un client dans des applications basées sur le Web. Acrobat JavaScript implémente des extensions, sous la forme de nouveaux objets et de leurs méthodes et propriétés associées, au langage JavaScript. Ces objets spécifiques à Acrobat permettent à un développeur de gérer la sécurité des documents, de communiquer avec une base de données, de gérer des pièces jointes, de manipuler un fichier PDF afin qu'il se comporte comme un formulaire interactif et activé par le Web, etc. Étant donné que les objets spécifiques à Acrobat sont ajoutés au-dessus de JavaScript de base, vous avez toujours accès à ses classes standard, y compris Math, String, Date, Array et RegExp.

### Acrobat JavaScript vs JavaScript HTML (Web)

Les documents PDF ont une grande polyvalence car ils peuvent être affichés à la fois dans le logiciel Acrobat et dans un navigateur Web. Par conséquent, il est important d'être conscient des différences entre Acrobat JavaScript et JavaScript utilisé dans un navigateur Web, également connu sous le nom de JavaScript HTML :

- Acrobat JavaScript n'a pas accès aux objets d'une page HTML. De même, JavaScript HTML ne peut pas accéder aux objets d'un fichier PDF.
- JavaScript HTML peut manipuler des objets tels que Window. Acrobat JavaScript ne peut pas accéder à cet objet particulier mais peut manipuler des objets spécifiques aux PDF.

Vous pouvez ajouter JavaScript à la fois au niveau du document et de la page en utilisant [Aspose.PDF for .NET](/pdf/net/). Pour ajouter JavaScript :

### Ajouter JavaScript à l'action du document ou de la page

1. Déclarez et instanciez un objet JavascriptAction avec l'instruction JavaScript souhaitée comme argument du constructeur.
1. Assignez l'objet JavascriptAction à l'action souhaitée du document ou de la page PDF.

L'exemple ci-dessous applique l'OpenAction à un document spécifique.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Adding JavaScript at Document Level
        // Instantiate JavascriptAction with desired JavaScript statement
        var javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

        // Assign JavascriptAction object to desired action of Document
        document.OpenAction = javaScript;

        // Adding JavaScript at Page Level
        document.Pages[2].Actions.OnOpen = new JavascriptAction("app.alert('page 1 opened')");
        document.Pages[2].Actions.OnClose = new JavascriptAction("app.alert('page 1 closed')");

        // Save PDF Document
        document.Save(dataDir + "JavaScriptAdded_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Adding JavaScript at Document Level
    // Instantiate JavascriptAction with desired JavaScript statement
    var javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

    // Assign JavascriptAction object to desired action of Document
    document.OpenAction = javaScript;

    // Adding JavaScript at Page Level
    document.Pages[2].Actions.OnOpen = new JavascriptAction("app.alert('page 1 opened')");
    document.Pages[2].Actions.OnClose = new JavascriptAction("app.alert('page 1 closed')");

    // Save PDF Document
    document.Save(dataDir + "JavaScriptAdded_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### Ajouter/Retirer JavaScript au niveau du document

Une nouvelle propriété nommée JavaScript est ajoutée dans la classe Document qui a un type de collection JavaScript et fournit un accès aux scénarios JavaScript par sa clé. Cette propriété est utilisée pour ajouter du JavaScript au niveau du document. La collection JavaScript a les propriétés et méthodes suivantes :

- string this(string key)– Obtient ou définit JavaScript par son nom.
- IList Keys – fournit une liste des clés existantes dans la collection JavaScript.
- bool Remove(string key) – supprime JavaScript par sa clé.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.Pages.Add();
        document.JavaScript["func1"] = "function func1() { hello(); }";
        document.JavaScript["func2"] = "function func2() { hello(); }";
        document.Save(dataDir + "AddJavascript.pdf");
    }

    // Remove Document level JavaScript
    using (var document1 = new Aspose.Pdf.Document(dataDir + "AddJavascript.pdf"))
    {
        var keys = (IList)document1.JavaScript.Keys;

        Console.WriteLine("=============================== ");

        foreach (string key in keys)
        {
            Console.WriteLine(key + " ==> " + document1.JavaScript[key]);
        }

        document1.JavaScript.Remove("func1");

        Console.WriteLine("Key 'func1' removed ");
        Console.WriteLine("=============================== ");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    document.Pages.Add();
    document.JavaScript["func1"] = "function func1() { hello(); }";
    document.JavaScript["func2"] = "function func2() { hello(); }";
    document.Save(dataDir + "AddJavascript.pdf");

    // Remove Document level JavaScript
    using var document1 = new Aspose.Pdf.Document(dataDir + "AddJavascript.pdf");
    IList keys = (IList)document1.JavaScript.Keys;

    Console.WriteLine("=============================== ");

    foreach (string key in keys)
    {
        Console.WriteLine(key + " ==> " + document1.JavaScript[key]);
    }

    document1.JavaScript.Remove("func1");

    Console.WriteLine("Key 'func1' removed ");
    Console.WriteLine("=============================== ");
}
```
{{< /tab >}}
{{< /tabs >}}

### Définir la date d'expiration d'un document PDF à l'aide d'actions JavaScript

Aspose.PDF vous permet de définir une date d'expiration pour un document PDF en intégrant des actions JavaScript. Cette fonctionnalité garantit que le PDF devient inaccessible après une date et une heure spécifiées, améliorant ainsi la sécurité et le contrôle des documents. En tirant parti des actions JavaScript, vous pouvez définir des conditions d'expiration précises jusqu'à la seconde, garantissant que l'accessibilité du document est étroitement régulée.

**Vous pouvez y parvenir en suivant ces étapes**

1. **Initialiser le Document :** Créez un nouveau document PDF et ajoutez une page vierge ou ouvrez un document PDF existant.
2. **Définir la Date et l'Heure d'Expiration :** Définissez la date et l'heure après lesquelles le document expirera.
3. **Préparer le Code JavaScript :** 
    - Récupérez la date et l'heure actuelles.
    - Définissez la date et l'heure d'expiration exactes, en tenant compte que les mois sont basés sur zéro en JavaScript.
    - Comparez la date et l'heure actuelles avec la date et l'heure d'expiration.
    - Si la date et l'heure actuelles dépassent la date et l'heure d'expiration, affichez une alerte et fermez le document.
4. **Définir l'Action d'Ouverture :** Associez l'action JavaScript à l'action d'ouverture du document.
5. **Enregistrer le Document :** Enregistrez le PDF avec le JavaScript intégré qui impose la condition d'expiration.

Ci-dessous se trouvent des extraits de code démontrant cette fonctionnalité en C# (.NET) et en Java.

L'extrait de code C# suivant démontre comment définir une date et une heure d'expiration pour un document PDF en utilisant des actions JavaScript avec Aspose.PDF :

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocumentWithExpiryDate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.Pages.Add();

        // Define the expiry date and time (e.g., April 1, 2025, 12:00:00 PM)
        DateTime expiryDateTime = new DateTime(2025, 4, 1, 12, 0, 0);

        // Create JavaScript code to enforce the expiry date and time
        string jsCode =
            // Get the current date and time
            "var rightNow = new Date();\n" +
            // Set the expiry date and time
            "var endDate = new Date(" +
            $"{expiryDateTime.Year}," +
            $"{expiryDateTime.Month - 1}," + // Months are zero-based in JavaScript
            $"{expiryDateTime.Day}," +
            $"{expiryDateTime.Hour}," +
            $"{expiryDateTime.Minute}," +
            $"{expiryDateTime.Second}" +
            ");\n" +
            "if(rightNow > endDate)\n" +
            "{\n" +
            "    app.alert(\"This Document has Expired as of \" + endDate.toLocaleString() + \".\");\n" +
            "    this.closeDoc();\n" +
            "}";

        // Create a JavascriptAction with the defined JavaScript code
        var javaScript = new Aspose.Pdf.Annotations.JavascriptAction(jsCode);

        // Set the JavaScript action to execute when the document is opened
        document.OpenAction = javaScript;

        // Save PDF document
        document.Save(dataDir + "PDFExpiry_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocumentWithExpiryDate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    document.Pages.Add();

    // Define the expiry date and time (e.g., April 1, 2025, 12:00:00 PM)
    var expiryDateTime = new DateTime(2025, 4, 1, 12, 0, 0);

    // Create JavaScript code to enforce the expiry date and time
    string jsCode =
        // Get the current date and time
        "var rightNow = new Date();\n" +
        // Set the expiry date and time
        "var endDate = new Date(" +
        $"{expiryDateTime.Year}," +
        $"{expiryDateTime.Month - 1}," + // Months are zero-based in JavaScript
        $"{expiryDateTime.Day}," +
        $"{expiryDateTime.Hour}," +
        $"{expiryDateTime.Minute}," +
        $"{expiryDateTime.Second}" +
        ");\n" +
        "if(rightNow > endDate)\n" +
        "{\n" +
        "    app.alert(\"This Document has Expired as of \" + endDate.toLocaleString() + \".\");\n" +
        "    this.closeDoc();\n" +
        "}";

    // Create a JavascriptAction with the defined JavaScript code
    var javaScript = new Aspose.Pdf.Annotations.JavascriptAction(jsCode);

    // Set the JavaScript action to execute when the document is opened
    document.OpenAction = javaScript;

    // Save PDF document
    document.Save(dataDir + "PDFExpiry_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

- **Objet Date JavaScript :** En JavaScript, l'index du mois commence à `0` pour janvier et se termine à `11` pour décembre. Assurez-vous que la valeur du mois est ajustée en conséquence lors de la définition de la date et de l'heure d'expiration.
  
- **Considérations de Sécurité :** Bien que les actions JavaScript puissent contrôler le comportement d'un document PDF, elles dépendent du support du visualiseur PDF pour JavaScript. Tous les visualiseurs PDF ne peuvent pas honorer ces scripts, et les utilisateurs peuvent avoir désactivé l'exécution de JavaScript pour des raisons de sécurité.

- **Personnalisation :** Modifiez le code JavaScript pour effectuer des actions supplémentaires lors de l'expiration, telles que désactiver certaines fonctionnalités, rediriger vers une page spécifique ou enregistrer l'événement. De plus, si nécessaire, vous pouvez vérifier uniquement la date d'expiration sans spécifier l'heure.

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