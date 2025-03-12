---
title: Quelle est la différence entre les formats FDF, XML et XFDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /fr/net/whats-the-difference-between-xml-fdf-and-xfdf/
description: Cette section explique la différence entre les formulaires XML, FDF et XFDF avec les façades Aspose.PDF en utilisant la classe Form.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Whats is the difference between FDF, XML, and XFDF formats",
    "alternativeHeadline": "Understanding FDF, XML, and XFDF Formats in Aspose.PDF for .NET",
    "abstract": "Découvrez les différences entre les formats FDF, XML et XFDF dans la manipulation des données de formulaire PDF à travers Aspose.PDF for .NET. Cette fonctionnalité permet aux développeurs d'exporter sans effort les valeurs des champs de formulaire interactifs dans divers formats, chacun avec sa propre syntaxe, tout en améliorant la compréhension et l'utilisation de ces types de fichiers essentiels dans le traitement des PDF. Optimisez votre gestion des formulaires PDF avec des informations détaillées sur la manière de représenter les champs de formulaire à travers différents formats de données.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1045",
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
    "url": "/net/whats-the-difference-between-xml-fdf-and-xfdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/whats-the-difference-between-xml-fdf-and-xfdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

{{% alert color="primary" %}}

Nous avons mélangé de nombreux termes différents comme FDF, XML et XFDF. Tous ces termes sont liés les uns aux autres d'une certaine manière. Cet article explore ces concepts et leur relation entre eux.

{{% /alert %}}

## Déchiffrer les formulaires

Aspose.PDF for .NET est utilisé pour manipuler des documents PDF standardisés par Adobe. Et les documents PDF contiennent des formulaires interactifs appelés AcroForms. Ces formulaires interactifs ont un certain nombre de champs de formulaire, comme des listes déroulantes, des zones de texte et des boutons radio. Les formulaires interactifs d'Adobe et les champs de formulaire fonctionnent de la même manière qu'un formulaire HTML et ses champs de formulaire.

Il est possible de stocker les valeurs des champs de formulaire dans un fichier séparé : un fichier FDF (Forms Data Format). Cela contient les valeurs des champs de formulaire sous forme de paires clé/valeur. Les fichiers FDF sont encore utilisés à cette fin. Mais Adobe fournit également un type de FDF encodé en XML appelé XFDF. Un fichier XFDF stocke les valeurs des champs de formulaire de manière hiérarchique en utilisant des balises XML.

Avec Aspose.PDF, les développeurs peuvent non seulement exporter les valeurs des champs de formulaire PDF vers un fichier FDF ou XFDF, mais aussi vers un fichier XML. Tous ces fichiers utilisent une syntaxe différente pour enregistrer les valeurs des champs de formulaire PDF. L'exemple ci-dessous explique les différences.

Supposons qu'il y ait des champs de formulaire PDF dont les valeurs doivent être présentées sous forme de FDF, XML et XFDF. Ces champs de formulaire supposés avec leurs noms de champ et valeurs sont montrés ci-dessous :

|**Nom du champ**|**Valeur du champ**|
| :- | :- |
|Société|Aspose.com|
|Adresse.1|Sydney, Australie|
|Adresse.2|Ligne d'adresse supplémentaire|
Voyons comment représenter ces valeurs dans les formats FDF, XML et XFDF.

### Qu'est-ce que le format FDF ?

Comme nous le savons, le fichier FDF stocke les données sous forme de paires clé/valeur où /T représente une clé, /V représente la valeur et les données entre parenthèses () représentent le contenu d'une clé ou d'une valeur. Par exemple, /T(Company) signifie que Company est la clé de champ et /V(Aspose.com) est destiné à une valeur de champ.

/T(Company) /V(Aspose.com)
/T(Address.1) /V( Sydney , Australie )
/T(Address.2) /V(Ligne d'adresse supplémentaire)

### Qu'est-ce que le format XML ? 

Les développeurs peuvent représenter chaque champ de formulaire PDF sous la forme d'une balise de champ, `<field>`. Chaque balise de champ a un attribut, name, qui montre le nom du champ et une sous-balise, `<value>`, représentant la valeur du champ comme montré ci-dessous :

```xml
 <?xml version="1.0" ?>
 <fields>
  <field name="Company">
    <value>Aspose.com</value>
  </field>
  <field name="Address.1">
    <value>Sydney, Australia</value>
  </field>
  <field name="Address.2">
    <value>Additional Address Line</value>
  </field>
 </fields>
```

### Qu'est-ce que le format XFDF ?  

La représentation des données ci-dessus sous forme XFDF est similaire à celle du format XML, sauf pour quelques différences. Dans les fichiers XFDF, nous ajoutons leur espace de noms XML, qui est <http://ns.adpbe.com/xfdf/> et il y a une balise supplémentaire, `<f>`, qui est utilisée pour pointer vers le document PDF contenant ces champs de formulaire PDF. Comme XML, XFDF contient également des champs sous forme de balises de champ, `<field>`, comme montré ci-dessous :

```xml

<?xml version="1.0" encoding="UTF-8"?>
<xfdf xmlns="http://ns.adobe.com/xfdf/" xml:space="preserve">   
   <f href="CompanyForm.pdf"/> 
   <fields>
      <field name="Company">
         <value>Aspose.com</value>
      </field>
      <field name="Address">
         <field name="1">
            <value>Sydney, Australia</value>
         </field>
         <field name="2">
            <value>Additional Address Line</value>
         </field>
      </field>
   </fields>
 </xfdf>
```

### Identification des noms des champs de formulaire

Aspose.PDF for .NET offre la possibilité de créer, modifier et remplir des formulaires PDF déjà créés. Il contient la classe [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form), qui a la fonction nommée [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index), et elle prend deux paramètres, c'est-à-dire le nom du champ qui doit être rempli et la valeur du champ. Donc, pour remplir les champs de formulaire, vous devez être conscient du nom exact du champ de formulaire.
Nous rencontrons souvent le scénario dans lequel nous devons remplir le formulaire qui a été créé dans un outil, c'est-à-dire Adobe Designer, et nous ne sommes pas sûrs des noms des champs de formulaire. Pour accomplir notre besoin, nous devons lire les noms de tous les champs de formulaire PDF. La classe [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) fournit la propriété nommée [FieldsNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames) qui retourne tous les noms de champs et retourne null si le PDF n'a pas de champ. Mais cette propriété renverra tous les noms des champs de formulaire PDF et nous ne saurons pas quel nom correspond à quel champ sur le formulaire.

Comme solution à ce problème, nous aurions besoin des attributs d'apparence de chaque champ. La classe [Form](http://www.aspose.com/documentation/file-format-components/aspose.pdf.kit-for-.net-and-java/aspose.pdf.kit.form.html) a une fonction nommée GetFieldFacade qui retourne des attributs, y compris la localisation, la couleur, le style de bordure, la police, les éléments de liste, etc. Pour enregistrer ces valeurs, nous utiliserons la classe [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade), qui est utilisée pour enregistrer les attributs visuels des champs. Une fois que nous avons ces attributs, nous pouvons ajouter un champ de texte sous chaque champ qui afficherait le nom du champ. Ici, une question se pose : comment déterminerions-nous l'emplacement où ajouter le champ de texte ? La solution à ce problème est la propriété Box dans la classe [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade), qui contient la localisation du champ. Nous enregistrerons ces valeurs dans un tableau de type rectangle et utiliserons ces valeurs pour identifier la position où ajouter les nouveaux champs de texte.
Dans l'espace de noms Aspose.Pdf.Facades, nous avons une classe nommée [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) qui offre la capacité de manipuler les formulaires PDF. Ouvrez un formulaire PDF, ajoutez un champ de texte sous chaque champ de formulaire existant et enregistrez le formulaire PDF avec un nouveau nom.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DifferenceBetweenFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // First a input pdf file should be assigned
    using (var form = new Aspose.Pdf.Facades.Form(dataDir + "FilledForm.pdf"))
    {
        // Get all field names
        String[] allfields = form.FieldNames;
        // Create an array which will hold the location coordinates of Form fields
        var box = new System.Drawing.Rectangle[allfields.Length];
        for (int i = 0; i < allfields.Length; i++)
        {
            // Get the appearance attributes of each field, consecutively
            var facade = form.GetFieldFacade(allfields[i]);
            // Box in FormFieldFacade class holds field's location.
            box[i] = facade.Box;
        }
        // Save PDF document
        form.Save(dataDir + "DifferenceBetweenFile_out.pdf");
            
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "FilledForm - 2.pdf"))
        {
            // Now we need to add a textfield just upon the original one
            FormEditor editor = new Aspose.Pdf.Facades.FormEditor(document);
            for (int i = 0; i < allfields.Length; i++)
            {
                // Add text field beneath every existing form field
                editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "TextField" + i, allfields[i], 1, box[i].Left, box[i].Top, box[i].Left + 50, box[i].Top + 10);
            }
            // Save PDF document
            editor.Save(dataDir + "DifferenceBetweenFile_out.pdf");
        }
    }
}
```