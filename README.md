# “Fifty Shades of Bias”: Normative Ratings of Gender Bias in GPT
Generated English Text

Language serves as a powerful tool for the manifestation of societal belief systems. In doing so, it also perpetuates the prevalent biases in our society. Gender bias is one of the most pervasive biases in our society and is seen in online and offline discourses. With LLMs increasingly gaining human-like fluency in text generation, gaining a nuanced understanding of the biases these systems can generate is imperative. Prior work often treats gender bias as a binary classification task. However, acknowledging that bias must be perceived at a relative scale; we investigate the generation and consequent receptivity of manual annotators to bias of varying degrees. Specifically, we create the first dataset of GPT-generated English text with normative ratings of gender bias. Ratings were obtained using Best–Worst Scaling – an efficient comparative annotation framework. Next, we systematically analyze the variation of themes of gender biases in the observed ranking and show that identity-attack is most closely related to gender bias. Finally, we show the performance of existing automated models trained on related concepts on our dataset.

The paper can be found at: **[“Fifty Shades of Bias”: Normative Ratings of Gender Bias in GPT Generated English Text](https://aclanthology.org/2023.emnlp-main.115.pdf)**

Our online talk at EMNLP’23 can be found [here](https://screenpal.com/watch/c0lY1oVHlrm).

If you use our work, please cite us:

```bash
@inproceedings{hada-etal-2023-fifty,
    title = "{``}Fifty Shades of Bias{''}: Normative Ratings of Gender Bias in {GPT} Generated {E}nglish Text",
    author = "Hada, Rishav  and
      Seth, Agrima  and
      Diddee, Harshita  and
      Bali, Kalika",
    editor = "Bouamor, Houda  and
      Pino, Juan  and
      Bali, Kalika",
    booktitle = "Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2023",
    address = "Singapore",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.emnlp-main.115",
    doi = "10.18653/v1/2023.emnlp-main.115",
    pages = "1862--1876",
    abstract = "Language serves as a powerful tool for the manifestation of societal belief systems. In doing so, it also perpetuates the prevalent biases in our society. Gender bias is one of the most pervasive biases in our society and is seen in online and offline discourses. With LLMs increasingly gaining human-like fluency in text generation, gaining a nuanced understanding of the biases these systems can generate is imperative. Prior work often treats gender bias as a binary classification task. However, acknowledging that bias must be perceived at a relative scale; we investigate the generation and consequent receptivity of manual annotators to bias of varying degrees. Specifically, we create the first dataset of GPT-generated English text with normative ratings of gender bias. Ratings were obtained using Best{--}Worst Scaling {--} an efficient comparative annotation framework. Next, we systematically analyze the variation of themes of gender biases in the observed ranking and show that identity-attack is most closely related to gender bias. Finally, we show the performance of existing automated models trained on related concepts on our dataset.",
}
```

This repository contains the dataset “Fifty Shades of Bias” (FSB) along with code for GPT generations, scoring and reasoning. The repository is structured as follows:

```bash
.
├── CODE_OF_CONDUCT.md
├── LICENSE
├── README.md
├── SECURITY.md
├── SUPPORT.md
├── data
│   ├── FSB
│   │   ├── FSB_text.csv
│   │   ├── fsb-tuples-annotations.csv
│   │   └── fsb_final_scores.csv
│   ├── in_context_examples
│   │   ├── explicit_completion_ic.json
│   │   ├── explicit_conversion_ic.json
│   │   ├── implicit_completion_ic.json
│   │   ├── implicit_conversion_ic.json
│   │   ├── neutral_completion_ic.json
│   │   └── neutral_conversion_ic.json
│   └── seeds
│       ├── explict_bias_seed.txt
│       ├── implicit_bias_seed.txt
│       └── neutral_bias_seed.txt
├── FSB_Underline.pdf
├── index.html
├── requirements.txt
├── scripts
│   ├── generate_biased_sentences.py
│   ├── gpt_reasoning.py
│   ├── gpt_scoring.py
│   └── utils.py
└── tree.md
```

- **Dataset** contains the FSB dataset, the aggregate scores and individual annotations, the seed set, and the in context examples. *Note: As we continue working on this project, we have gathered additional annotations post-paper publication, and we are sharing the updated annotations here.*
- **Scripts** contains the code for GPT generations, scoring, and reasoning.
- `requirements.txt` lists down the requirements for running the code on the repository. The requirements can be installed using : `pip install -r requirements.txt`
- `index.html` contains the code for the annotation task interface.

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
