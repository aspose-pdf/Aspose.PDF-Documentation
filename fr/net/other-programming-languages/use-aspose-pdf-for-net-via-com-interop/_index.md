---
title: Aspose.PDF pour .NET via COM Interop
type: docs
weight: 20
url: /fr/net/use-aspose-pdf-for-net-via-com-interop/
---

{{% alert color="primary" %}}

Les informations dans ce sujet s'appliquent aux scénarios où vous souhaitez utiliser [Aspose.PDF pour .NET](/pdf/fr/net/) via COM Interop dans l'un des langages de programmation suivants :

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

## Travailler avec COM Interop

Aspose.PDF pour .NET s'exécute sous le contrôle du Framework .NET et cela est appelé code géré. Le code écrit dans tous les langages ci-dessus fonctionne en dehors du Framework .NET et il est appelé code non géré. L'interaction entre le code non géré et Aspose.PDF se fait via une fonctionnalité de .NET appelée COM Interop.

Les objets Aspose.PDF sont des objets .NET, mais lorsqu'ils sont utilisés via COM Interop, ils apparaissent comme des objets COM dans votre langage de programmation.
Les objets Aspose.PDF sont des objets .NET, mais lorsqu'ils sont utilisés via COM Interop, ils apparaissent comme des objets COM dans votre langage de programmation.

{{% alert color="primary" %}}

- Dans le monde COM, nous distinguons le serveur COM et le client COM. Le serveur COM stocke les classes COM tandis que le client COM demande au serveur COM des instances de classes, c'est-à-dire des objets COM.
- Le client COM ou simplement l'application cliente peut connaître quelque chose sur le contenu de la classe COM ou être totalement ignorant de ses méthodes et propriétés. Par conséquent, l'application cliente peut découvrir la structure de la classe COM lors de la compilation/construction ou uniquement pendant l'exécution. Le processus de "découverte" est connu sous le nom de liaison et donc nous avons la **liaison anticipée** et la **liaison tardive**.
- En bref, la classe COM est comme une boîte noire et pour travailler avec elle, une bibliothèque de types est nécessaire, ce fichier binaire a une description des méthodes, des propriétés de la classe COM et tout langage de haut niveau qui prend en charge le travail avec les objets COM a souvent une expression syntaxique pour ajouter une bibliothèque de types, par exemple ceci est [**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx) en C++.
- En bref, une classe COM est comme une boîte noire et pour travailler avec elle, une bibliothèque de types est nécessaire. Ce fichier binaire contient la description des méthodes, des propriétés de la classe COM et tout langage de haut niveau qui prend en charge le travail avec les objets COM a souvent une expression syntaxique pour ajouter une bibliothèque de types, par exemple ceci est [**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx) en C++.
- La bibliothèque de types est utilisée pour la liaison anticipée.
- Un objet COM peut exposer ses méthodes et propriétés de deux manières : au moyen d'une **interface de dispatch** (dispinterface) et dans sa **table de fonctions virtuelles** (vtable).
- Au sein de l'**interface de dispatch**, chaque méthode et propriété est identifiée par un membre unique ; ce membre est l'identifiant de dispatch de la fonction (ou **DispID**).
- La **table de fonctions virtuelles** n'est qu'un ensemble de pointeurs vers des fonctions que l'interface de classe COM prend en charge.
- Un objet qui expose ses méthodes à travers les deux interfaces prend en charge une **interface double**.
- Il y a des avantages aux deux types de liaison.
- il existe des avantages aux deux types de liaison.
- le mécanisme de liaison tardive a un grand avantage : si le créateur de la DLL COM décide de sortir une nouvelle version, avec une disposition d'interface de fonction différente, tout code appelant ces méthodes ne plantera pas à moins que les méthodes ne soient plus disponibles ; même si la **vtable** est différente, la liaison tardive parvient à découvrir les nouveaux DISPIDs et à appeler les méthodes appropriées.
{{% /alert %}}

Voici les sujets que vous devrez éventuellement maîtriser :
{{% alert color="primary" %}}

- Utiliser des objets COM dans votre langage de programmation. Consultez la documentation de votre langage de programmation et les sujets spécifiques au langage plus loin dans cette documentation.

- Travailler avec des objets COM exposés par .NET COM Interop. Voir [Interoperating With Unmanaged Code](http://msdn.microsoft.com/en-us/library/sd10k43k.aspx) et [Exposing .NET Framework Components to COM](http://msdn.microsoft.com/en-us/library/zsfww439%28v=vs.110%29.aspx) dans MSDN.

- Modèle objet de document Aspose.PDF.
- Modèle objet de document Aspose.PDF.

{{% /alert %}}

## Enregistrer Aspose.PDF pour .NET avec COM Interop

Vous devez installer Aspose.PDF pour .NET et vous assurer qu'il est enregistré avec COM Interop (ce qui garantit qu'il peut être appelé à partir de code non géré).

{{% alert color="primary" %}}

Pour enregistrer manuellement Aspose.PDF pour .NET pour COM Interop :

1. Depuis le menu **Démarrer**, sélectionnez **Tous les programmes**, puis **Microsoft Visual Studio**, **Outils Visual Studio** et, enfin, **Invite de commandes Visual Studio**.
1. Entrez la commande pour enregistrer l'assemblage :
   1. .NET Framework 2.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net2.0\Aspose.PDF.dll" /codebase
   1. .NET Framework 3.5
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net3.5\Aspose.PDF.dll" /codebase
   1. .NET Framework 4.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.0\Aspose.PDF.dll" /codebase

{{% /alert %}}

Notez que /codebase est nécessaire seulement si Aspose.PDF.dll n'est pas dans GAC, utiliser cette option permet à regasm de mettre le chemin de l'assemblage dans le registre.
Faites attention, /codebase est nécessaire uniquement si Aspose.PDF.dll n'est pas dans le GAC, utiliser cette option permet à regasm de mettre le chemin de l'assemblage dans le registre.

{{% alert color="primary" %}}

regasm.exe est un outil inclus dans le SDK .NET Framework. Tous les outils du SDK .NET Framework se trouvent dans le répertoire *\Microsoft .NET\Framework\<VersionDuFramework>*, par exemple *C:\Windows\Microsoft .NET\Framework\v4.0.30319*. Si vous utilisez Visual Studio .NET :
Depuis le menu **Démarrer**, sélectionnez **Programmes**, suivi de **Microsoft Visual Studio .NET**, puis **Outils Visual Studio .NET** et, enfin, **Invite de commandes Visual Studio .NET 2003**.
Il exécute une invite de commandes avec toutes les variables d'environnement nécessaires définies.

{{% /alert %}}

### ProgIDs

ProgID signifie "identifiant programmatique". C'est le nom d'une classe COM utilisée pour créer un objet. Les ProgIDs se composent du nom de la bibliothèque "Aspose.PDF" et du nom de la classe.

### Bibliothèque de types

{{% alert color="primary" %}}

Si votre langage de programmation (par exemple Visual Basic ou Delphi) vous permet de référencer une bibliothèque de types COM, alors ajoutez une référence à Aspose.PDF.tlb pour voir toutes les classes, méthodes, propriétés et énumérations de Aspose.PDF pour .NET dans votre navigateur d'objets.
Si votre langage de programmation (par exemple Visual Basic ou Delphi) vous permet de référencer une bibliothèque de types COM, ajoutez alors une référence à Aspose.PDF.tlb pour voir toutes les classes, méthodes, propriétés et énumérations d'Aspose.PDF pour .NET dans votre explorateur d'objets.

Pour générer un fichier TLB :

- .NET Framework 2.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net2.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net2.0\Aspose.PDF.tlb" /codebase
- .NET Framework 3.5
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net3.5\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net3.5\Aspose.PDF.tlb" /codebase
- .NET Framework 4.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.0\Aspose.PDF.tlb" /codebase

{{% /alert %}}

## Création d'objets COM

La création d'un objet COM est similaire à la création d'un objet .NET normal :

```vb

'Instancier une instance de Pdf en appelant son constructeur vide

Dim pdf
Set pdf = CreateObject("Aspose.PDF.Generator.Pdf")

```
Une fois créé, vous pouvez accéder aux méthodes et propriétés de l'objet, comme s'il s'agissait d'un objet COM :

```vb
' Ajouter une section à l'objet Pdf
pdf.Sections.Add(pdfsection)
```

Certaines méthodes ont des surcharges et elles seront exposées par COM Interop avec un suffixe numérique ajouté, sauf pour la toute première méthode qui reste inchangée. Par exemple, les surcharges de la méthode Pdf.Save deviennent Pdf.Save, Pdf.Save_2, et ainsi de suite.

Pour plus d'informations, consultez les articles spécifiques à la langue plus loin dans cette documentation.

## Création d'un Assembly Wrapper

Si vous avez besoin d'utiliser de nombreuses classes, méthodes et propriétés de Aspose.PDF pour .NET, envisagez de créer un assembly wrapper (en utilisant C# ou tout autre langage de programmation .NET). Les assemblies wrapper aident à éviter d'utiliser directement Aspose.PDF pour .NET à partir de code non géré.

Une bonne approche consiste à développer un assembly .NET qui référence Aspose.PDF pour .NET et qui effectue tout le travail avec, et expose uniquement un ensemble minimal de classes et de méthodes au code non géré.
Une bonne approche consiste à développer un assembly .NET qui référence Aspose.PDF pour .NET et qui effectue tout le travail avec, en exposant seulement un ensemble minimal de classes et de méthodes au code non géré.

Réduire le nombre de classes et de méthodes que vous devez invoquer via COM Interop simplifie le projet. Utiliser des classes .NET via COM Interop nécessite souvent des compétences avancées.
