import streamlit as st

def calculate_missing_values(args):
    for key in args:
        if args[key] == -1:
            args[key] = None
    # Calculate LP $ value
    if args['eth_pool'] is not None and args['token_pool'] is not None:
        args['lp_value'] = 2 * args['eth_pool']
    elif args['lp_value'] is not None:
        args['eth_pool'] = args['lp_value'] / 2
        args['token_pool'] = args['lp_value'] / 2

    # Calculate Token Price
    if args['token_price'] is None and args['token_pool'] is not None and args['eth_pool'] is not None:
        args['token_price'] = args['eth_pool'] / args['token_pool']

    # Calculate Market Cap
    if args['mcap'] is None and args['token_price'] is not None and args['supply'] is not None:
        args['mcap'] = args['token_price'] * args['supply']
    elif args['mcap'] is not None and args['token_price'] is not None:
        args['supply'] = args['mcap'] / args['token_price']

    return args

def main():
    st.title('Fintool - Uniswap ERC20 Token')

    args = {
        'supply': st.number_input('Total Supply', value=-1),
        'mcap': st.number_input('Market Cap', value=-1),
        'token_pool': st.number_input('Pooled Tokens', value=-1),
        'eth_pool': st.number_input('Pooled Eth $', value=-1),
        'token_price': st.number_input('Token Price', value=-1),
        'lp_value': st.number_input('LP $ Value', value=-1)
    }

    if st.button('Calculate'):
        args = calculate_missing_values(args)

        st.write(f"Total Supply: {args['supply']}")
        st.write(f"Market Cap: {args['mcap']}")
        st.write(f"Pooled Tokens: {args['token_pool']}")
        st.write(f"Pooled Eth $: {args['eth_pool']}")
        st.write(f"Token Price: {args['token_price']}")
        st.write(f"LP $ Value: {args['lp_value']}")

if __name__ == '__main__':
    main()
