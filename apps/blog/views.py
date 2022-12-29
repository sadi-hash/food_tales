from django.shortcuts import render

from django.views.generic import TemplateView, ListView,DeleteView
# Create your views here.

from apps.blog.models import Category, Post

# CVB - Class Based Views - Вьюшки на классах
class IndexPage(TemplateView):
    template_name = "index.html"

# # Function Based Views = Вьюшки основанные на функциях
# def index_page(requests):
#     return  render(requests,"index.html")







class ProductsView(TemplateView):
    template_name = "products.html"




class CategoryListView(ListView):
    template_name = "category_list.html"
    model = Category
    queryset = Category.objects.all()




def get_categories(request):
    categories = Category,object.all()
    context = {
        "categories":categories
    }
    return render(request, 'categpry_list.html', context)

class PostListView(ListView):
    template_name ="post_list.html"
    model = Post
    queryset = Post.objects.filter(is_draft=False)


    # отправка данных в шаблон через данный метод 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_posts = Post.objects.filter(is_draft=False).order_by("-created")
        if len(latest_posts) <4:
            context["latest_posts"] = latest_posts
        else:
            context["latest_posts"] = latest_posts[:4]    
        
        context["categories"] = Category.objects.all()

        return context



    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        if category_slug:
            qs = Post.objects.filter(is_draft=False, category__slug=category_slug)
            return qs
        return Post.objects.filter(is_draft=False)


class PostDetailView(DeleteView):
    template_name = "post_detail.html"  
    model = Post   



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_posts = Post.objects.filter(is_draft=False).order_by("-created")
        if len(latest_posts) <4:
            context["latest_posts"] = latest_posts
        else:
            context["latest_posts"] = latest_posts[:4]    
        
        context["categories"] = Category.objects.all()

        return context
 



# Как бы выглядела логика , если бы писали на функциях 
# def get_detail_post(request,pk):
#     try:
#         post = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#         pass
#     context = {
#         "post":post
#     }
#     return render(request, 'post_detail.html', context=context)
