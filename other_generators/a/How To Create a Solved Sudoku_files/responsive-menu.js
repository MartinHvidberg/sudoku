;(function($){

    $.fn.mobileMenuCollapse = function(options){
	
		var mmSettings = {};
	
		var init = function(){
            
			mmSettings['collapsed'] = false;
			$('#menu-collapsed').on('click', function(e){
				
                console.log($(e.target).attr('id') );
				if ( $(e.target).attr('id') == 'collapsed-menu-head') {
					if ( e.preventDefault ){
						e.preventDefault();
					}else{
						e.returnValue = false;
					}
					$('#menu-collapsed ul').toggle('slow');
				}

			});		
		};
      console.log('initializing');
		init();
		//return this;
	};

}(jQuery));
