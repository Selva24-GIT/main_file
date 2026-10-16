from django.shortcuts import render

# Create your views here.

prod=[
        {'id':1,
         'article_subtitle':'Stock Market — NSE debuts at ₹1,818 while Indian stocks suffer a broad sell-off',

         'article_img': "/image/cover_img.png",

         'content':'''Reported facts — September 24: National Stock Exchange of India listed at ₹1,800, versus its ₹1,785 IPO price, 
         and closed its first session at ₹1,818, a 1.85% gain. Its closing market value was reported at about ₹4.49 lakh crore. � Rediff
         At the same time, India's broader market had a difficult session: the Sensex fell 1,247.71 points (1.67%) to 73,580.54, while the Nifty 50 
         fell 1.64% to 23,063.10. Brent crude rose to about $105.40/barrel, adding pressure to the oil-importing Indian economy. �
         DD India
         Why it matters: NSE's debut is a major investment-market event, but the same-day sell-off shows why an individual IPO must be considered alongside
         macro conditions, oil prices and interest rates.''',

         'second_content':''' Lorem ipsum dolor sit, amet consectetur adipisicing elit. Saepe, facilis. Quaerat voluptates impedit maxime
            aliquam, velit accusamus hic, illum nemo ipsam molestias voluptatem et officia, modi beatae doloremque
            repellat Lorem ipsum, dolor sit amet consectetur adipisicing elit. Veniam modi quo facere, ducimus maiores provident accusamus aut velit 
            necessitatibus perspiciatis. Lorem ipsum dolor sit amet consectetur adipisicing elit. Rerum repellendus sint esse voluptas voluptatem nobis. 
            Natus, maxime nisi? Ad, enim!'''

         },

         {'id':2,
          'article_subtitle':'Programming — GitHub adds Grok 4.7 to its AI coding platform',

          'article_img': "/image/cover_img3.png",

          'content':'''Reported facts — September 21: GitHub began rolling out Grok 4.7 from xAI inside GitHub Copilot. It is designed for agentic coding 
          and multi-step workflows and can be selected in environments including VS Code, Visual Studio, Copilot CLI and JetBrains. �GitHub Blog 
          GitHub has also recently added multiple competing models to Copilot, including GPT-6 Astra, Gemini 3.8 Flash and Claude Fable 5.1. �GitHub Blog +2 
          Why it matters for learning: Coding assistants are becoming multi-model development platforms, where developers choose an AI model depending on the task.
          FACT: GitHub says the Grok 4.7 rollout is gradual and availability depends on the Copilot plan. �
           ''',

            'second_content':''' ANALYSIS: For someone learning Python, JavaScript, React or Django, 
                      the valuable skill isn't memorising one AI tool. It's learning how to prompt, inspect, 
                      test and debug AI-generated code.GitHub Blog
                      Learning takeaway: Treat AI as a coding assistant—not as a replacement for understanding your program.'''
          },
         {'id':3,
           'article_subtitle':'AI — OpenAI and Anthropic call for global AI safety standards',

          'article_img': "/image/cover_img4.png",

           'content':'''Reported facts — September 23–24: OpenAI CEO Sam Altman and Anthropic CEO Dario Amodei addressed the UN Security 
           Council on AI and international security. They called for international cooperation and common standards for testing advanced AI systems, 
           including testing for misuse and loss-of-control risks. �The Guardian +1
           Why it matters: AI governance is moving beyond individual companies and governments toward a global-security discussion.
           FACT: The UN meeting took place on September 23; it did not produce a binding international agreement. �
           ANALYSIS: Common testing standards could make AI safety claims more comparable, but geopolitical competition may make agreement difficult.''',

             'second_content':''' Lorem ipsum dolor sit, amet consectetur adipisicing elit. Saepe, facilis. Quaerat voluptates impedit maxime
                       aliquam, velit accusamus hic, illum nemo ipsam molestias voluptatem et officia, modi beatae doloremque
                       repellat Lorem ipsum, dolor sit amet consectetur adipisicing elit. Veniam modi quo facere, ducimus maiores provident accusamus aut velit 
                       necessitatibus perspiciatis. Lorem ipsum dolor sit amet consectetur adipisicing elit. Rerum repellendus sint esse voluptas voluptatem nobis. 
                       Natus, maxime nisi? Ad, enim!'''
          },
    ]

def abt(request):
    return  render(request,"abt.html")

def product(request,id):   
    for i in prod:
        if i['id']==id:
            data=i
    return  render(request,"product.html",{'key':data})

def demo(request,id):
    for i in prod:
        if i['id']==id:
            data=i
    return render(request,"demo.html",{'key':data})