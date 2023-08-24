# factuality-eval
Companion code and iPython notebooks for evaluating factuality as outlined
in this [blog post](https://www.anyscale.com/blog/llama-2-is-about-as-factually-accurate-as-gpt-4-for-summaries-and-is-30x-cheaper) 
on "Can you trust Llama 2 and ChatGPT to factually summarize?"

Please contact mwk+factuality@anyscale.com if you have any questions. 

Parts of the code included here are extracted from an experimental library called [Hermetic](https://github.com/anyscale/hermetic). 
For simplicity, the code in this repo is self-contained and does not have any dependencies on that library. 


For convenience, this code is self-contained. 

To get started: 
```python
% pip install -r requirements.txt
```

You also need to ensure that you have an OPENAI_API_KEY and AE_API_KEY. 
Include these in the environment variables. 

Once that's complete, you can run the notebook. 


# Supporting files
The `val_sentence_pairs.json` is from TU Delft: 

```
@misc{https://tudatalib.ulb.tu-darmstadt.de/handle/tudatalib/2002,
url = { https://tudatalib.ulb.tu-darmstadt.de/handle/tudatalib/2002 },
author = { Falke, Tobias and Ribeiro, Leonardo and utama, caraka prasetya and Dagan, Ido and Gurevych, Iryna },
keywords = { 000 Informatik, Informationswissenschaft, allgemeine Werke },
publisher = { Technical University of Darmstadt },
year = { 2019-06-04 },
copyright = { Creative Commons Attribution Share-Alike 4.0 },
title = { Correctness of Generated Summaries }
}
```

In the `resources` folder we included three versions of the prompts where we experimented with: 

* Asking for the answer last (to give time for reasoning)
* Deliberately calling out the bias and asking for it to work. 

These addiitonal experiments did not have a major impact on the results; it seem that each 
different version of these queries were in "tradeoff" territory where it changed the individual
results but not the outcomes. 




