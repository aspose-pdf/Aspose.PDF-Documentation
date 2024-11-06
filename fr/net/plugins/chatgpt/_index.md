---
title: ChatGPT
type: docs
weight: 30
url: fr/net/plugins/chatGPT/
description: Comment générer des réponses ChatGPT alimentées par l'IA et les stocker en PDF
lastmod: "2024-02-24"
---

## Générer des réponses de chat alimentées par IA avec le plugin ChatGpt

Vous avez déjà voulu améliorer vos documents PDF avec des réponses de chat générées par l'IA ? Ne cherchez plus ! Dans ce guide, nous allons vous montrer comment intégrer le puissant [plugin ChatGpt](https://products.aspose.org/pdf/net/chat-gpt/) dans votre application C#. Avec seulement quelques étapes simples, vous générerez des réponses de chat captivantes sans effort.

## Prérequis

Vous aurez besoin de ce qui suit :

* Visual Studio 2019 ou ultérieur
* Aspose.PDF pour .NET 24.1 ou ultérieur
* Un fichier PDF d'exemple

## Étapes

### 1. Création d'un objet

Commençons par créer un objet pour notre tâche de génération de chat. Le morceau de code C# fourni montre comment configurer les options pour le plugin PdfChatGpt.

```csharp
// Créer des options pour le plugin ChatGPT.
var options = new PdfChatGptRequestOptions();
```
### 2. Ajout d'une source de données

Ensuite, nous devons ajouter une source de données, qui dans ce cas, est le fichier PDF d'entrée contenant le texte que vous souhaitez améliorer avec des réponses de chat générées par l'IA.

```csharp
// Ajouter le fichier PDF d'entrée aux options.
options.AddInput(new FileDataSource("c:\\Samples\\sample.pdf"));

// Ajouter le fichier PDF de sortie aux options.
options.AddOutput(new FileDataSource("c:\\Samples\\chat_results.pdf"));
```

Dans l'extrait de code ci-dessus, nous spécifions le chemin du fichier PDF d'entrée et le chemin de sortie où le PDF amélioré avec des réponses de chat sera sauvegardé.

### 3. Exécution de la méthode Process

Maintenant, mettons tout en action en exécutant la méthode de processus. C'est là que la magie opère – le modèle ChatGPT alimenté par l'IA génère des réponses de chat basées sur la requête et le texte fournis.

```csharp
// Définir la clé API pour l'authentification.
options.ApiKey = "sk-******";

// Définir le nombre maximum de jetons pour le modèle ChatGPT.
options.MaxTokens = 1000;

// Définir la requête pour le modèle ChatGPT.
options.Query = "Quels sont les meilleurs mots-clés pour ce texte ?";

// Créer une instance du plugin PdfChatGpt.
var plugin = new PdfChatGpt();

// Traiter le document PDF en utilisant le plugin ChatGPT.
var result = await plugin.ProcessAsync(options);
```
Avec ces lignes de code, nous configurons l'authentification, définissons les paramètres pour le modèle ChatGPT, et lançons le processus de génération de chat.
