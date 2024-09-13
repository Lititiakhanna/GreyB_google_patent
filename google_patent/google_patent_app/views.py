from django.shortcuts import render
from django.db.models.functions import ExtractYear, Cast
from django.db.models import IntegerField
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CategoricalFrequencyCount, GooglePatentData, NumericalStatistics

class SummaryAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            numerical_stats = NumericalStatistics.objects.all()
            categorical_freq_counts = CategoricalFrequencyCount.objects.all()
            if not numerical_stats and not categorical_freq_counts:
                return Response({'message': 'Summary not found'}, status=status.HTTP_404_NOT_FOUND)
            data = {
                'Numerical features summary-number of viewers':{numerical_stat.index: numerical_stat.number_of_viewers for numerical_stat in numerical_stats} if numerical_stats else {},
                'Categorical features summary-number of authors': {categorical_freq_count.category: categorical_freq_count.count for categorical_freq_count in categorical_freq_counts} if categorical_freq_counts else {}
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response({'message': 'unexpected error occured'}, status=status.HTTP_400_BAD_REQUEST)

class QueryPatentView(APIView):
    def get(self, request, *args, **kwargs):

        patent_year = request.query_params.get('patent_year')
        if patent_year:
            try:
                patents = GooglePatentData.objects.filter(publication_date__startswith=patent_year)

                if patents.exists():
                    data = {
                        f'Patent Year: {patent_year}':[{'Patent ID': patent.id,
                                                        'Patent Title': patent.title,
                                                        'Assignee': patent.assignee,
                                                        'Priority Date': patent.priority_date,
                                                        'Creation Date': patent.creation_date,
                                                        'Patent Date': patent.publication_date,
                                                        'Grant Date': patent.grant_date,
                                                        'Result Link': patent.result_link,
                                                        'Representative Figure Link': patent.representative_figure_link,
                                                        'Number of Authors': patent.number_of_authors,
                                                        'Number of Viewers': patent.number_of_viewers} for patent in patents]
                    }
                    return Response(data, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "No patents found for the year provided."}, status=status.HTTP_404_NOT_FOUND)
            except Exception:
                return Response({"message": "Invalid year format."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "patent_year query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)