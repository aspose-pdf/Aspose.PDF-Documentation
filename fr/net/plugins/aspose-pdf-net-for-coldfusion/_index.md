---
title: Utiliser Aspose.Pdf pour .NET avec Coldfusion
type: docs
weight: 300
url: /fr/net/using-aspose-pdf-for-net-with-coldfusion/
description: Vous devriez travailler avec Aspose.Pdf pour .NET avec Coldfusion en utilisant la classe PdfFileInfo
lastmod: "2021-07-14"
draft: false
---

{{% alert color="primary" %}}

Dans cet article, nous expliquerons comment utiliser Aspose.PDF pour .NET avec Coldfusion. Cela vous aidera à comprendre les détails de l'intégration de Aspose.PDF pour .Net et Coldfusion. À l'aide d'un exemple simple, je vous montrerai le processus d'intégration de la fonctionnalité de Aspose.PDF pour .Net dans vos applications Coldfusion.

{{% /alert %}}

## Contexte

Aspose.PDF pour .NET est un composant qui offre également la capacité d'éditer et de manipuler des fichiers PDF existants.
Aspose.PDF pour .NET est un composant qui offre également la capacité de modifier et de manipuler des fichiers PDF existants.

## Prérequis

Pour pouvoir exécuter Aspose.PDF pour .Net avec Coldfusion, vous aurez besoin d'IIS, .Net 2.0 et Coldfusion. J'ai testé le composant en utilisant IIS 5, .Net 2.0 et Coldfusion 8. Il y a deux autres choses dont vous devez vous assurer lors de l'installation de Coldfusion. Premièrement, vous devez spécifier quel(s) site(s) sous IIS exécutera Coldfusion. Deuxièmement, vous devrez sélectionner 'Services d'intégration .Net' dans l'installateur Coldfusion. Les Services d'intégration .Net vous permettent d'accéder à l'assemblage de composants .Net dans les applications Coldfusion ; dans ce cas, le composant sera Aspose.PDF pour .NET.

## Explication

Tout d'abord, vous devez copier le DLL (Aspose.PDF .dll) à un emplacement d'où vous y accéderez plus tard ; cela sera défini comme un chemin et attribué à l'attribut assembly de la balise cfobject comme indiqué ci-dessous :

```html
<cfobject type = ".NET" name = "fileinfo" 
        class = "Aspose.PDF.Facades.PdfFileInfo" 
        assembly = "C:/Aspose/Net/Assembly/Aspose.PDF.dll">
```
L'attribut de classe dans la balise ci-dessus pointe vers la classe Aspose.PDF. Facades, qui dans ce cas est PdfFileInfo. L'attribut nom est le nom de l'instance de la classe et sera utilisé plus tard dans le code pour accéder aux méthodes ou propriétés de la classe. L'attribut type spécifie le type de composant - dans notre cas, il s'agit de .Net.

Un point important que vous devrez garder à l'esprit lors de l'utilisation du composant .Net dans Coldfusion est que, lorsque vous obtenez ou définissez une propriété de l'objet classe, vous devez suivre une structure spécifique. Pour définir une propriété, vous utiliserez la syntaxe Set_nompropriete, et pour obtenir une valeur de propriété, vous utiliserez Get_nompropriete.

Par exemple

Définir une valeur de propriété :

```html
<cfset FilePath = ExpandPath("guide.pdf")>
```

Obtenir une valeur de propriété :

```html
<cfoutput>#fileinfo.Get_title()#</cfoutput>
```

Un exemple de base mais complet pour vous aider à comprendre le processus d'utilisation d'Aspose.PDF pour .NET dans Coldfusion est donné ci-dessous.

### Montrons les informations du fichier PDF

```html
<!--- créer une instance de la classe PdfFileInfo --->

<cfobject type = ".NET" name = "fileinfo" class = "Aspose.PDF.Facades.PdfFileInfo"

assembly = "C:/Aspose/Net/Assembly/Aspose.PDF.dll">

<!--- obtenir le chemin du fichier pdf --->

<cfset FilePath = ExpandPath("guide.pdf")>

<!--- assigner le chemin du fichier pdf à l'objet classe en définissant sa propriété inputfile --->

<cfset fileinfo.Set_inputfile(FilePath)>

<!--- Montrer les informations du fichier --->

<cfoutput><b>Titre:</b>#fileinfo.Get_title()#</cfoutput><br/>
<cfoutput><b>Sujet:</b>#fileinfo.Get_subject()#</cfoutput><br/>
<cfoutput><b>Auteur:</b>#fileinfo.Get_author()#</cfoutput><br/>
<cfoutput><b>Créateur:</b>#fileinfo.Get_Creator()#</cfoutput><br/>

```
## Conclusion

{{% alert color="primary" %}}
Dans cet article, nous avons vu que si nous suivons quelques règles de base de l'intégration de Coldfusion et .Net, nous pouvons intégrer de nombreuses fonctionnalités et flexibilités liées à la manipulation de documents PDF, en utilisant Aspose.PDF pour .NET dans nos applications Coldfusion.
{{% /alert %}}
