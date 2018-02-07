var rootapp = angular.module('rootapp', ['ngRoute']);


rootapp.config(function ($routeProvider,$locationProvider) {
    
    $routeProvider
    
    .when('/wfh', {
        
        templateUrl: static_url + 'shiftroster/html/wfhform.html',
        controller: 'wfhController'
    })
    
    .when('/tcr', {
        
        templateUrl: static_url + 'shiftroster/html/tcrform.html',
        controller: 'tcrController'
    })
    
     $locationProvider.html5Mode(true);
    
});


rootapp.controller('wfhController', function($scope,$http){
    $scope.$location = {};
$('#wfhForm').slideToggle();
$('#tcrForm').css('display', 'none');
 //$('#wfhForm').dblclick='index.htm';
});

//var tcrapp = angular.module('tcrapp',[]);
rootapp.controller('tcrController',function($scope,$http){
    $scope.$location = {};
$('#tcrForm').slideToggle();
$('#wfhForm').css('display', 'none');
 
});
    
