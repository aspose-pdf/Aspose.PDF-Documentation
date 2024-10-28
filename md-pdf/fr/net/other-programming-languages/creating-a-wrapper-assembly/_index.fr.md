---
title: Création d'un Assembly de Contournement
type: docs
weight: 80
url: /net/creating-a-wrapper-assembly/
---

{{% alert color="primary" %}}

Si vous avez besoin d'utiliser de nombreuses classes, méthodes et propriétés d'Aspose.PDF pour .NET, envisagez de créer un assembly de contournement (en utilisant C# ou tout autre langage de programmation .NET). Les assemblies de contournement aident à éviter d'utiliser directement Aspose.PDF pour .NET depuis du code non géré.

Une bonne approche consiste à développer un assembly .NET qui référence Aspose.PDF pour .NET et effectue tout le travail avec, et n'expose qu'un ensemble minimal de classes et de méthodes au code non géré. Votre application doit alors fonctionner uniquement avec votre bibliothèque de contournement.

Réduire le nombre de classes et de méthodes que vous devez invoquer via COM Interop simplifie le projet. Utiliser des classes .NET via COM Interop nécessite souvent des compétences avancées.

{{% /alert %}}

## Wrapper Aspose.PDF pour .NET

```csharp

using System;
using System.Runtime.InteropServices;
namespace PdfText
{
    [Guid("FC969AC9-6591-46FB-A4AB-DB12A776F3BF")]
    [InterfaceType(ComInterfaceType.InterfaceIsIDispatch)]
    public interface IPetriever
    {
        [DispId(1)]
        void SetLicense(string file);

        [DispId(2)]
        string GetText(string file);
    }

    [Guid("3D59100F-3CC5-463D-B509-58FA0520B436")]
    [ClassInterface(ClassInterfaceType.None)]

    [ComSourceInterfaces(typeof(IPetriever))]

    public class Petriever : IPetriever
    {
        public void SetLicense(string file)
        {
            License lic = new License();
            lic.SetLicense(file);
        }

        public string GetText(string file)
        {
            // ouvrir le document
            Document doc = new Document(file);

            // créer un objet TextAbsorber pour extraire le texte
            TextAbsorber absorber = new TextAbsorber();

            // accepter l'absorbeur pour toutes les pages du document
            doc.Pages.Accept(absorber);

            // obtenir le texte extrait

            string text = absorber.Text;
            return text;

        }
    }
}

```

