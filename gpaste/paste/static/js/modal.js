/* Courtesy of https://github.com/codrops/ModalWindowEffects for effects and JS */

function classReg( className ) {
  return new RegExp("(^|\\s+)" + className + "(\\s+|$)");
}

var hasClass = function( elem, c ) {
    return classReg( c ).test( elem.className );
};

var addClass = function( elem, c ) {
    if ( !hasClass( elem, c ) ) {
        elem.className = elem.className + ' ' + c;
    }
};

var removeClass = function( elem, c ) {
    elem.className = elem.className.replace( classReg( c ), ' ' );
};

var ModalEffects = (function() {

	function init() {

		var overlay = document.querySelector( '.md-overlay' );

		[].slice.call( document.querySelectorAll( '.md-trigger' ) ).forEach( function( el, i ) {

			var modal = document.querySelector( '#' + el.getAttribute( 'data-modal' ) ),
				close = modal.querySelector( '.close' );

			function removeModal( hasPerspective ) {
				removeClass( modal, 'md-show' );
				removeClass( overlay, 'md-show' );
			}

            function removeModalHandler() {
				removeModal( hasClass( el, 'md-setperspective' ) );
			}

			el.addEventListener( 'click', function( ev ) {
				addClass( modal, 'md-show' );
                addClass( overlay, 'md-show' );
				overlay.removeEventListener( 'click', removeModalHandler );
				overlay.addEventListener( 'click', removeModalHandler );
			});

			close.addEventListener( 'click', function( ev ) {
				ev.stopPropagation();
                removeModalHandler();
			});

		} );

	}

	init();

})();
