from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, project_pk=None):
        pass

    def post(self, request):
        pass

    def put(self, request, pk, project_pk):
        pass
    
    def patch(self, request, pk, project_pk):
        pass

    def delete(self, request, pk, project_pk):
        pass

class CommentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, project_pk=None):
        pass

    def post(self, request):
        pass

    def put(self, request, pk, project_pk):
        pass
    
    def patch(self, request, pk, project_pk):
        pass

    def delete(self, request, pk, project_pk):
        pass
