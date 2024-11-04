---
title: Quelle est la différence entre les formats FDF, XML et XFDF
type: docs
weight: 30
url: /net/whats-the-difference-between-xml-fdf-and-xfdf/
description: Cette section explique la différence entre les formulaires XML, FDF et XFDF avec Aspose.PDF Facades en utilisant la classe Form.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Nous avons mélangé de nombreux termes différents comme FDF, XML et XFDF. Tous ces termes sont liés les uns aux autres d'une certaine manière. Cet article explore ces concepts et leur relation entre eux.

{{% /alert %}}

## Démystifier les formulaires

Aspose.PDF pour .NET est utilisé pour manipuler des documents PDF standardisés par Adobe. Et les documents PDF contiennent des formulaires interactifs appelés AcroForms. Ces formulaires interactifs ont un certain nombre de champs de formulaire, comme la liste déroulante, la zone de texte et le bouton radio. Les formulaires interactifs d'Adobe et les champs de formulaire fonctionnent de la même manière qu'un formulaire HTML et ses champs de formulaire.

Il est possible de stocker les valeurs des champs de formulaire dans un fichier séparé : un fichier FDF (Forms Data Format). Ce document contient les valeurs des champs de formulaire sous forme de paires clé/valeur. Les fichiers FDF sont toujours utilisés à cet effet. Mais Adobe propose également un type FDF encodé en XML appelé XFDF. Un fichier XFDF stocke les valeurs des champs de formulaire de manière hiérarchique en utilisant des balises XML.

Avec Aspose.PDF, les développeurs peuvent non seulement exporter les valeurs des champs de formulaire PDF vers un fichier FDF ou XFDF, mais aussi vers un fichier XML. Tous ces fichiers utilisent une syntaxe différente pour enregistrer les valeurs des champs de formulaire PDF. L'exemple ci-dessous explique les différences.

Supposons qu'il y ait certains champs de formulaire PDF dont les valeurs doivent être présentées sous forme FDF, XML et XFDF. Ces champs de formulaire supposés avec leurs noms de champs et valeurs sont montrés ci-dessous :

|**Nom du champ**|**Valeur du champ**|
| :- | :- |
|Company|Aspose.com|
|Address.1|Sydney, Australia|
|Address.2|Additional Address Line|
Voyons comment représenter ces valeurs dans les formats FDF, XML et XFDF.

### Qu'est-ce que le format FDF ?

Comme nous le savons, le fichier FDF stocke les données sous forme de paires Clé/Valeur où /T représente une Clé, /V représente la Valeur et les données entre parenthèses () représentent le contenu d'une Clé ou d'une Valeur. /T(Company) /V(Aspose.com)
/T(Address.1) /V( Sydney , Australia )
/T(Address.2) /V(Ligne d'adresse supplémentaire)

### Qu'est-ce que le format XML ? 

Les développeurs peuvent représenter chaque champ de formulaire PDF sous la forme d'une balise de champ, `<field>`. Chaque balise de champ a un attribut, name, montrant le nom du champ et une sous-balise, `<value>` représentant la valeur du champ comme indiqué ci-dessous :

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
    <value>Ligne d'adresse supplémentaire</value>
  </field>
 </fields>
```

### ### Qu'est-ce que le format XFDF ?  

La représentation des données ci-dessus sous forme XFDF est similaire à la forme XML à quelques différences près. Dans les fichiers XFDF, nous ajoutons leur espace de nom XML, qui est <http://ns.adpbe.com/xfdf/> et il y a une balise supplémentaire, `<f>` qui est utilisée pour pointer vers le document PDF contenant ces champs de formulaire PDF. Comme XML, XFDF contient également des champs sous forme de balises de champ, `<field>` comme indiqué ci-dessous :

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

Aspose.PDF pour .NET offre la possibilité de créer, modifier et remplir des formulaires PDF déjà créés. Il contient la classe [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form), qui a la fonction nommée [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index), et elle prend deux paramètres, c'est-à-dire le nom du champ à remplir et la valeur du champ. Donc, pour remplir les champs du formulaire, vous devez connaître le nom exact du champ du formulaire. Nous rencontrons souvent le scénario dans lequel nous devons remplir le formulaire qui est créé dans un outil i.e. Adobe Designer, et nous ne sommes pas sûrs des noms des champs du formulaire. Pour répondre à notre besoin, nous devons lire les noms de tous les champs de formulaire PDF. La classe [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) fournit la propriété nommée [FieldsNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames) qui retourne tous les noms des champs et retourne null si le PDF n'a pas de champ. Mais cette propriété renverra tous les noms des champs du formulaire PDF et nous ne serons pas sûrs de quel nom correspond à quel champ sur le formulaire.

Comme solution à ce problème, nous aurions besoin des attributs d'apparence de chaque champ. [Form](http://www.aspose.com/documentation/file-format-components/aspose.pdf.kit-for-.net-and-java/aspose.pdf.kit.form.html) classe a une fonction nommée GetFieldFacade qui renvoie des attributs, y compris l'emplacement, la couleur, le style de bordure, la police, l'élément de liste, etc. Pour enregistrer ces valeurs, nous utiliserons la classe [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade), qui est utilisée pour enregistrer les attributs visuels des champs. Une fois que nous avons ces attributs, nous pouvons ajouter un champ de texte sous chaque champ qui afficherait le nom du champ. Ici, une question se pose : comment déterminer l'emplacement où ajouter le champ de texte ? La solution à ce problème est la propriété Box dans la classe [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade), qui contient l'emplacement du champ. Nous enregistrerions ces valeurs dans un tableau de type rectangle et utiliserions ces valeurs pour identifier la position où ajouter les nouveaux champs de texte. Dans l'espace de noms Aspose.Pdf.Facades, nous avons une classe nommée [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) qui offre la capacité de manipuler le formulaire PDF. Ouvrez un formulaire PDF, ajoutez un champ de texte sous chaque champ de formulaire existant et enregistrez le formulaire PDF avec un nouveau nom.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-DifferenceBetweenFile-DifferenceBetweenFile.cs" >}}