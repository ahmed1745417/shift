var rootapp = angular.module('rootapp', ['ngRoute']);


rootapp.config(function ($routeProvider) {
    
    $routeProvider
    
    .when('/wfh', {
        
        templateUrl: 'wfhform.html',
        controller: 'wfhController'
    })
    
    .when('/tcr', {
        
        templateUrl: 'tcrform.html',
        controller: 'tcrController'
    })
    
    .otherwise({
        
    })
    
});

//var wfhapp = angular.module('wfhapp',[]);
rootapp.controller('wfhController', function($scope,$http){
    $scope.show_form = true;
// Function to add toggle behaviour to form

$('#wfhForm').slideToggle();
$('#tcrForm').css('display', 'none');
 $('#wfhForm').dblclick='index.htm';
});

//var tcrapp = angular.module('tcrapp',[]);
rootapp.controller('tcrController',function($scope,$http){
$scope.show_form1 = true;
    // Function to add toggle behaviour to form

$('#tcrForm').slideToggle();
$('#wfhForm').css('display', 'none');
 
});
    
